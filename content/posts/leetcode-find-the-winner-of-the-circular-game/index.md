+++
title = 'LeetCode 60 天挑戰 D08 - Find the Winner of the Circular Game'
date = 2024-07-09T00:05:14+08:00
draft = false
tags = ['LeetCode']
+++

今天是第 8 天，也是我實習的第 1 天，早上以為時間很充裕就悠閒地吃著早餐，結果搭公車到松山站差點沒趕上接駁車，車門都關上了，好險司機再等行人過馬路。

原本搭公車的時候還很緊張，不知道第一天要怎麽面對別人，不過 insta 跳出久沒聯絡的朋友的訊息頓時安心不少，雖然內容和實習無關哈哈。

實習第 1 天蠻無聊的，前半天都在認識環境和其他人，後半天因為在等 MIS 團隊用 GitHub 帳號，結果也沒辦法做什麼事情，只能裝裝軟體就發呆等下班。不過和我同個 team 的另外兩三位實習生看起來人都不錯 (nice)，不知道能力怎麽樣就是了。

是說公司的服務竟然沒有上 k8S，不知道這在業界算不算常見...

總之還是先多看多學好了。

連結: [1823. Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/)

今天是 Medium，不過我也不知道為什麽這算是 Medium...

大意是說有一群人圍成一圈編號 1 到 n，每次隔 k 個去把人刪掉，直到刪到剩下一個人，回傳他的編號。

基本上就是跟著敘述一個一個人慢慢數，遇到第 k 個再把他刪掉，最後再回傳剩下的那一個人就可以過了，畢竟最差也才 n square (k = n)。

```py3
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        exist = [ True ] * n
        total = n
        walk = 0 # 0-indexed
        count = k
        while total > 1:
            if exist[walk] == True:
                count -= 1
                if count == 0:
                    exist[walk] = False
                    total -= 1
                    count = k
            walk = (walk + 1) % n
        for i in range(n):
            if exist[i] == True:
                return i + 1
        return -1
```
