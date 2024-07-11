+++
title = 'LeetCode 60 天挑戰 D11 - Reverse Substrings Between Each Pair of Parentheses'
date = 2024-07-12T00:58:08+08:00
draft = false
tags = ['LeetCode']
+++

今天是第 11 天，WFH 真的舒服，而且我效率還比較高，但是我還是不太會寫 Java。

下午原本在做一個打 outbound api 的練習一直失敗，我找了我的程式碼看有沒有錯誤找了兩個小時，結果最後發現根本不是程式問題，而是我 outbound api 的格式沒寫好，昏倒。

架構上我還是覺得目前寫的有點混亂，不太知道怎麽切會比較好看，明天再煩惱吧...

連結: [1190. Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/)

今天是 Medium，但其實也不難，寫到現在看到括弧基本上就會知道是 stack 了。

我的解法除非是 `)` 否則就丟到一個 stack 裡面，然後每當遇到 `)` 就把 `(` 和 `)` 之間的字母倒過來再放回去 (括弧順便拿掉)。

```py3
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop() # '('
                stack.extend(temp)
            else:
                stack.append(c)
        return ''.join(stack)
```
