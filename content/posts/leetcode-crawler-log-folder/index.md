+++
title = 'LeetCode 60 天挑戰 D10 - Crawler Log Folder'
date = 2024-07-11T01:28:43+08:00
draft = false
tags = ['LeetCode']
+++

今天是第 10 天，實習好累，不過明後天都是 WFH 所以不用早起了^^

一整天都還在用實習的查書 API 練習，覺得最阻撓我的是各種不熟悉 JPA，不然換個別的語言早寫完相同功能了...

而且我原本是用 Specification，但是因為我不想用 ManyToMany 所以搞半天要重寫改用 Query，幸好剛剛搞出來了，明早至少有點東西可以回報。

連結: [1598. Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/description/)

今天又是水水的 Easy 題，大意是說你會有一個字串陣列，每個都是 `'./'`，`'directory/'`，`'../'` 三選一，分別代表原目錄、進入某個目錄、回父目錄，然後如果是在根目錄就回父目錄就還是會停在原地。然後你要回傳你在的深度 (要花多少步回到根目錄)。

解法基本上就也是照著做就好了。

```py3
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log.startswith('..'):
                if depth != 0:
                    depth -= 1
            elif not log.startswith('.'):
                depth += 1
        return depth
```
