+++
title = 'JRE、JDK 差別在哪裡？'
date = 2024-06-14T21:45:59+08:00
draft = false
tags = ['Java']
+++

Java 是一個物件導向的高階語言。

在編譯的時候，我們不會直接將原始碼 (.java) 編譯成 machine code 讓 CPU 執行，而是先轉換成能夠在 Java virtual machine (JVM) 上執行的 Byte code (.class)。

這種設計的好處是能夠更好的支援不同平台，並且在不同平台上不需要在重新編譯，只要該環境上有 JVM 即可執行該程式。

不過這樣設計也是有缺點的，例如因為執行時會需要先從 Byte code 轉成 machine code 所以在效能上會有損失，除此之外，機器要有 JVM 才能夠執行 Java 程式。

> 之後如果有空我會再研究一下 Java 使用到的 JIT (Just-in-time compilation) 技術，現在就先挖個坑。

## JRE

JRE(Java Runtime Environment) 除了前面提到的 JVM 以外還包含了 Java SE(Standard Edition) API。

Java SE API 涵蓋了各種基本、常用的函式庫，例如標準輸入/輸出、各式資料結構 (Collection)、JDBC(Java Database Connectivity)、Socket 等。

如果想要在電腦上執行 Java 程式，我們就必須要在電腦上安裝 JRE 來提供 Java 的執行環境。

## JDK

JDK(Java Development Kit) 主要是給 Java 程式的開發人員使用，除了提供執行環境的 JRE 以外，還加上了編譯器 (javac) 和一些開發工具 (例如 javadoc)。

因此，如果我們想要撰寫、開發 Java 程式，就需要安裝 JDK。

![JVM、JRE、JDK 關係](java.svg)

OpenJDK 是昇陽電腦 (Sun Microsystems) 在 2009 發布的開源版本的 JDK。

而 OpenJDK 目前最多人使用的發行版就屬 Eclipse 基金會維護的 [Eclipse Temurin (Adoptium)](https://adoptium.net/)，因此後續介紹如何安裝我會以這個發行版為主。

## 安裝 Eclipse Temurin 21 JDK

可以直接去[官方網站](https://adoptium.net/)下載，不過這邊我還是選擇透過我的作業系統 Mint 的套件管理工具來安裝，其他不同作業系統的安裝方式可以參考 https://adoptium.net/installation/linux。

```sh
sudo apt install -y wget apt-transport-https gpg
wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null
echo "deb https://packages.adoptium.net/artifactory/deb $(awk -F= '/^UBUNTU_CODENAME/{print$2}' /etc/os-release) main" | sudo tee /etc/apt/sources.list.d/adoptium.list
sudo apt update
sudo apt install temurin-21-jdk # LTS
```

