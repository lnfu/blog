+++
title = 'LeetCode 60 天挑戰 D05 - Find the Minimum and Maximum Number of Nodes Between Critical Points'
date = 2024-07-05T05:26:56Z
draft = false
tags = ['LeetCode']
+++

今天是挑戰第 5 天，昨晚發燒全身痠痛，希望身體可以趕快恢復才有力氣訓練...

連結: [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/)

今天也是 Medium，但是個人覺得只是 Easy 的程度，因為只要照著題目意思做一遍就可以了。

題目大意是說給定一個串列，要回傳 critical point 之間的距離的最小和最大值，如果只有一個或是沒有 critical point，就回傳 [-1, -1]。

critical point 定義是 local minima 或是 local maxima (也就是要比前後都大或是比前後都小)。

我的作法就是跑一遍串列，紀錄每個 critical point 的位置，然後距離最大值想當然就是最後一個減去最開始的值，距離最小值則是兩兩相減取最小那一個就好。

```py3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        step = 1
        prev = head
        walk = head.next
        record = []
        while walk.next != None:
            if walk.val < walk.next.val and walk.val < prev.val:
                # local minimum
                record.append(step)
            elif walk.val > walk.next.val and walk.val > prev.val:
                # local maximum
                record.append(step)
            prev = walk
            walk = walk.next
            step += 1
        if len(record) < 2:
            return [-1, -1]
        mini = record[-1] - record[0]
        for i in range(len(record) - 1):
            diff = record[i+1] - record[i]
            if diff < mini:
                mini = diff
        return [mini, record[-1] - record[0]]
```
