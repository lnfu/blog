+++
title = 'LeetCode 60 天挑戰 D02 - Intersection of Two Arrays II'
date = 2024-07-02T12:54:57+08:00
draft = false
tags = ['LeetCode']
+++

今天是 LeetCode 60 天挑戰第 2 天，也是輕輕鬆鬆的 Easy 題。

連結: [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)

題目大意是給定兩個整數陣列，要回傳一個陣列是他們兩個的交集 (會有重複的元素)，順序不影響。

我的方法是直接 sort 兩個陣列，然後從這兩個陣列的開頭 (最小) 慢慢對照，如果有一樣的就放到 `ans`，否則就把動比較小的那個 (因為比較小的已經不可能再另一個陣列會有和它相同的數字了)。

```py3
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        ans = []
        while True:
            if i >= len(nums1) or j >= len(nums2):
                return ans
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans
```

不過這樣的複雜度會是 nlogn，如果想要 linear 的解法可能就用個 counter 紀錄每個數字出現的次數吧。

首先先跑一遍第一個陣列紀錄的每個數字的出現次數。然後跑一遍第二個陣列，紀錄都有出現的次數 (也就是次數不能大於第一個陣列的次數)。

```py3
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter()
        intersec = Counter()
        for num in nums1:
            cnt1[num] += 1
        for num in nums2:
            if intersec[num] < cnt1[num]:
                intersec[num] += 1
        ans = []
        for num, cnt in intersec.items():
            for i in range(cnt):
                ans.append(num)
        return ans
```
