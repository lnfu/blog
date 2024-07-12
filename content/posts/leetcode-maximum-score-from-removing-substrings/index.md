+++
title = 'LeetCode 60 天挑戰 D12 - Maximum Score From Removing Substrings'
date = 2024-07-12T23:45:16+08:00
draft = false
tags = ['LeetCode']
+++

今天是第 12 天，今天實習的第一個練習基本上都快做好了，只差最後的測試還沒寫。可能等我再熟悉多一點 RabbitMQ 來寫一篇文章介紹好了！

連結: [1717. Maximum Score From Removing Substrings](https://leetcode.com/problems/maximum-score-from-removing-substrings/description/)

今天是也是 Medium 但也還是不難，跟昨天概念上差不多的題目。

題目大意是說給定一段字串，然後你可以把子字串 `"ab"` 刪除得到 x 分，以及把 `"ba"` 刪除得到 y 分，問你最大能得到多少分數。

如果像 `"baba"` 先把中間的 `"ab"` 刪除得到 `"ba"` 就可以再刪除，所以我們可以用 stack 來做這題。

解法基本上就是先看 x 和 y 誰比較大，如果 x 比較大就先遞迴把 `"ab"` 換掉再去遞迴換掉 `"ba"`，否則就順序相反。

```py3
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def recursiveReplace(c1, c2, value, s):
            ans = 0
            stack = []
            for c in s:
                if len(stack) != 0 and stack[-1] == c1 and c == c2:
                    ans += value
                    stack.pop()
                else:
                    stack.append(c)
            return ans, ''.join(stack)
        if x > y:
            p1, s = recursiveReplace("a", "b", x, s)
            p2, _ = recursiveReplace("b", "a", y, s)
        else:
            p1, s = recursiveReplace("b", "a", y, s)
            p2, _ = recursiveReplace("a", "b", x, s)
        return p1 + p2
```
