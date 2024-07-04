+++
title = 'LeetCode 60 天挑戰 D04 - Merge Nodes in Between Zeros'
date = 2024-07-04T03:35:03Z
draft = false
tags = ['LeetCode']
+++

今天是第四天，一起床就寫了 (雖然我很晚起...)。雖然是 Medium，但是我覺得蠻水的，可能有資料結構的概念就會算 Medium 吧。

連結: [2181. Merge Nodes in Between Zeros](https://leetcode.com/problems/merge-nodes-in-between-zeros/description/)

題目是說給一個串列，要把用 0 隔開的數字當作一組算總和，總和當作新的串列的節點，最後要返回新的串列。

另外有說明原本的串列頭尾都會是 0 並且不會有連續兩個 0 的節點，然後新的串列我們不用使用 0 隔開。

我的作法基本上就是跑一遍算總和，遇到 0 就新增節點並且把目前總和歸零，最後因為會多一個節點所以要把它刪掉 (`prev.next`)。

不過這樣不是 inplace 的作法，反正它沒有要求就不要麻煩自己了。

```py3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        newWalk = newHead
        prev = None
        walk = head.next
        total = 0
        while True:
            if walk == None:
                break
            if walk.val == 0:
                newWalk.val = total
                newWalk.next = ListNode()
                prev = newWalk
                newWalk = newWalk.next
                total = 0
            else:
                total += walk.val
            walk = walk.next
        prev.next = None
        return newHead
```
