+++
title = 'Postfix 設定 SMTP AUTH'
date = 2024-06-19T00:39:27+08:00
draft = false
+++

> 這篇文章只會著重在 SMTP AUTH，不會詳細說明如何使用 Postfix，可能之後有空再寫一篇吧。

在架設 SMTP server 的時候，為了不要讓它被壞人當作垃圾郵件的跳板，常常會限制只允許在同一個網路下的伺服器利用它來寄信，甚至是只允許在 SMTP server 這台機器上面的使用者寄信。

這樣做雖然可以避免 Open Relay，不過卻在某些情境下會造成麻煩。舉例來說，如果我們今天在外面，由於我們的 IP address 不在當初設定的網段下，因此就無法使用該 SMTP server 來寄信了。

這時候，如果我們單純加上目前的 IP address 到設定檔中也是不實際的作法，因為我們無法事先知道在外面會拿到什麼 IP address，總不可能每次都要加入，然後不使用後再刪除吧？

比較好的作法可能是使用 VPN 先連到內網後再來寄信。

不過，還有一個更方便的方式，也就是這篇想要介紹的 SMTP AUTH(authentication)。

SMTP AUTH 允許我們先透過使用者名稱、密碼進行認證，如果認證通過後就能夠用該 SMTP 來寄信。

不過 SMTP AUTH 並不在 SMTP 原本的 protocol，如果我們要使用這個功能，而是要靠其他的框架來實現這個功能。其中，比較有名的就是 SASL(Simple Authentication and Security Layer)。

SASL 允許我們在連線中進行使用者認證。要在 Postfix 使用 SASL 做 SMTP AUTH，我們需要依靠第三方的模組來實做，最常見的是 dovecot 和 Cyrus SASL，這篇我會以 dovecot 來示範。

## 檢查 Postfix 支援 dovecot

```
postconf -a # 檢查支援的 SASL server module
postconf -A # 檢查支援的 SASL client module
```

## 安裝 、設定 dovecot

以下擇一安裝即可：
```
sudo apt install dovecot-imapd # IMAP
sudo apt install dovecot-pop3d # POP3
```

編輯 `/etc/dovecot/conf.d/10-master.conf`。

```
unix_listener /var/spool/postfix/private/auth {
    mode = 0666
    user = postfix
    group = postfix
}
```

編輯 `/etc/dovecot/conf.d/10-auth`，設定認證的方式 (通常只要開啟 plain 和 login 即可)。

```
auth_mechanisms = plain login
```

## 設定 Postfix

在 `main.cf` 加入以下設定。

```
smtpd_sasl_auth_enable = yes # 啟用 SMTP AUTH
smtpd_sasl_type = dovecot
smtpd_sasl_path = private/auth
broken_sasl_auth_clients = yes # 支援一些較舊的 MUA
smtpd_sasl_authenticated_header = yes # optional
smtpd_sasl_security_options = noanonymous # 不可以使用匿名來授權
smtpd_recipient_restrictions = permit_mynetworks permit_sasl_authentecated reject_unauth_destination
```

## 補充：設定 TLS

最後四條記得根據自己的憑證和金鑰位置來設定。

```
smtpd_tls_security_level = may # none | may | encrypt (encrypt 代表強制要求使用 TLS)
smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache
tls_random_source = dev:/dev/urandom
smtpd_tls_received_header = yes
smtpd_tls_auth_only = yes
smtpd_tls_loglevel = 1

smtpd_tls_cert_file = /etc/postfix/certs/pbook-cert.pem
smtpd_tls_key_file = /etc/postfix/certs/pbook-key.pem
smtpd_tls_CAfile = /etc/postfix/certs/cacert.pem
smtpd_tls_CApath = /etc/ssl/certs/certs
```

## 補充：Base64 Encode/Decode 指令

```
perl -MMIME::Base64 -e 'print encode_base64("\0帳號\0密碼");'
perl -MMIME::Base64 -e 'print decode_base64("???");'
```

或是使用 base64 程式。

```
echo -en "\0帳號\0密碼" | base64
echo -en "???" | base64 -d
```

## 測試

```
HELO <hostname>
AUTH PLAIN <經過 Base64 的帳號密碼>
```

如果有顯示認證成功就代表設定正確 (也可以試試看故意打錯密碼)。

## 參考

- https://www.postfix.org/postconf.1.html
