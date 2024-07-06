+++
title = 'LeetCode 60 天挑戰 D06 - Pass the Pillow'
date = 2024-07-06T17:06:59Z
draft = false
tags = ['LeetCode']
+++

今天是第 6 天，也是差一點又忘記了 (太晚起床)，而且今天原本要設定網路讓我在台北還能夠連回來，結果發現我對 PPPoE 不太熟悉，專題可能先稍微放下好了，等下個週末再一次衝刺做...

連結: [2582. Pass the Pillow](https://leetcode.com/problems/pass-the-pillow/description/)

今天是 Easy，基本上會國中 (還是國小?) 數學就可以解了。

題目大意是說給兩個整數 n 和 time，順序是 1, 2, 3, 4, ..., n, n-1, n-2, n-3, ..., 1, 2, 3, ...，然後你要回傳經過 time 次後會是什麽數字。

稍微看一下就知道這會是一個 2(n-1) 為一組的循環，只是最後會需要再以 n-1 做鏡像。

```
+0, +1, +2, +3, ..., +(n-1) 或是 -(n-1), ..., -3, -2, -1, -0
```

```py3
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        m = 2*(n - 1)
        pos = time % m
        if pos == n - 1:
            return n
        elif pos < n:
            return pos + 1
        else:
            return m - pos + 1
```

其實也可以把 n - 1 歸到左邊或右邊，就可以更乾淨一些。

```py3
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        m = 2*(n - 1)
        pos = time % m
        if pos > n - 1:
            return m - pos + 1
        return pos + 1
```
