+++
title = 'LeetCode 60 天挑戰 D09 - Average Waiting Time'
date = 2024-07-09T21:39:43+08:00
draft = false
tags = ['LeetCode']
+++

今天是第 9 天，昨天又沒睡好了，加上昨天頭髮還沒吹乾就吹到風所以一整天頭有點痛，實習好累，依稀記得小時候被問到以後的工作條件時完全不會考慮離家近，這次上班發現這對我蠻重要的，當然如果可以完全 remote 那是最好。

今天的 LeetCode 我是早上剛進公司等開會時寫的，難度不高。

連結: [1701. Average Waiting Time](https://leetcode.com/problems/average-waiting-time/description/)

大意是說給一連串 `[arrival, time]` 的 pair，代表每個客人到達的時間和他的餐點製作需要花費的時間 (依序)，然後要回傳平均大家等待的時間。

因為是照順序來，基本上只要統計每個人等的時間加總再除上總人數就可以了，不過如果有餐點還在製作卻有人來的話，就要往下累加。

我的寫法是每次都用一個 last 變數計算往下累加到什麽時候，如果下一個客人在這個時間以後才到就可以重置。每位客人要等的時間就是累加後的時間減去他到達的時間。

```py3
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        last = 0
        total = 0
        for arrival, time in customers:
            if last <= arrival: # reset
                last = arrival
            last += time
            total += (last - arrival)
        return total / len(customers)
```
