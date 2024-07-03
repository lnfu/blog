+++
title = 'LeetCode 60 天挑戰 D03 - Minimum Difference Between Largest and Smallest Value in Three Moves'
date = 2024-07-03T16:31:34Z
draft = false
+++

今天是 LeetCode 60 天挑戰第三天，差一點就忘記了... 看來還是要一早更新完機器就來寫一下比較保險。

連結: [1509. Minimum Difference Between Largest and Smallest Value in Three Moves](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/)

題目大意是給定一個陣列，我們可以任意把三個數字改成另一個值，然後要讓最大和最小的數的差要是最小。

稍微花了時間想了一下，其實把數字的數值改掉就和把那個數字刪除是同樣的意思 (因為就是把它變成中間的數值就好)。

所以我們其實只要先把這個陣列排序過 (陣列長度最長 10^5 所以可以 nlogn 過)，然後把三個數字拿掉找出最小的就好。

更具體一點就是假設有 `n` 個數字，那麽我們只要每次去看 `i` 和 `i + (n - 3) - 1` 的差 (也就是 `n - 3` 個數字為一組)，如果這個差比目前紀錄的還要小就更新答案。

```py3
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = n - 3
        if n <= 4:
            return 0
        minValue = nums[n-1] - nums[0]
        for i in range(n-m+1):
            current = nums[i+m-1] - nums[i]
            if current < minValue:
                minValue = current
        return minValue
```
