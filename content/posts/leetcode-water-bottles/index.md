+++
title = 'LeetCode 60 天挑戰 D07 - Water Bottles'
date = 2024-07-08T00:49:55+08:00
draft = false
tags = ['LeetCode']
+++

今天是第 7 天，終於一個禮拜了，本來想說這個週末來久違的打個 contest 結果還是搞到沒時間哈哈 (逃避逃避)。

早上原本想說趕火車所以就不去舉重課了，結果最後也沒趕上火車，早知到會如此就還是去上個課了。

明天 (正確來說是今天) 要去實習，有點緊張，希望不要出包，真的感謝朋友借住台北，不然我還真的不知道怎麽辦 (好像似乎常常麻煩他...)

連結: [1518. Water Bottles](https://leetcode.com/problems/water-bottles/description/)

題目大意是說你有 `numBottles` 瓶水，然後喝完後每 `numExchange` 個空瓶可以再換一瓶水，問你最多可以喝多少瓶水。

Easy 題，基本上就照著題目敘述做就可以過了。

```py3
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        ans = 0
        while full > 0:
            ans += full
            empty += full
            # full = 0
            full = empty // numExchange
            empty = empty % numExchange
        return ans
```