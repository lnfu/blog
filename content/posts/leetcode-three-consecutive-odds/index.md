+++
title = 'LeetCode 60 天挑戰 D01 - Three Consecutive Odds'
date = 2024-07-01T12:48:18+08:00
draft = false
tags = ['LeetCode']
+++

今天是我的 LeetCode 60 天挑戰第一天，這個挑戰我每天都會寫 LeetCode daily challenge，希望能夠持續下去 ^^

今天的 daily challenge 是 Easy 難度，非常舒服。

連結: [1550. Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds/description/)

題目大意是說給一個整數陣列，如果這個陣列存在連續三個奇數就回傳 True，否則回傳 False。

解法的話沒什麼好說的，就是跑一遍確認而已。

```py3
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        for num in arr:
            if num % 2 == 1:
                odd_count += 1
            else:
                odd_count = 0
            if odd_count == 3:
                return True
        return False
```