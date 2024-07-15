+++
title = 'LeetCode 60 天挑戰 D14 - Number of Atoms'
date = 2024-07-16T00:18:46+08:00
draft = false
tags = ['LeetCode']
+++

補上昨天 (第 14 天) 沒紀錄到的。

這兩天實習加上專題快要累死了，雖然專題依然沒什麼進度，可能要找時間好好仔細地 trace 每個用到的 paper 的程式碼 (有點想自己自幹一個 Gaussian Splatting 哈哈)。

連結: [726. Number of Atoms](https://leetcode.com/problems/number-of-atoms/description/)

這次題目是 Hard，不過我覺得概念上不難，只是撰寫上比較麻煩一點而已。

題目是說給定一個化學式，你需要回傳一個字串，裡面內容是每個元素接上它出現的次數。

例如 `K4(ON(SO3)2)2` 就要回傳 `K4N2O14S4` (元素按字典序)。

我的想法是用一個 stack 來存所有經過的符號，然後每當遇到數字，就往回看，如果沒有括號就直接把前一個元素拿出來然後重複數字代表的次數，再放回 stack，如果有括號就先不斷 pop 直到遇到和他配對的左括號，然後對之間的所有符號重複。

不過因為數字可能是兩位數以上，所以我改成用一個 `num` 的陣列來存數字，然後遇到非數字在做前面提到的操作，然後我一開始有先把 `formula` 尾端加上一個 `$` 字號當作結尾，這樣讓程式碼比較乾淨 (就不用迴圈跑完還要再額外跑一次重複元素的操作)。

另外，因為像是 `Mg` 會佔兩格，所以遇到小寫的字母也要把他跟前面大寫的綁定在一起，不過因為最多只會接一個小寫，所以我們只要 pop 出大寫再接上小寫就好了。

等到跑過一遍把所有數字都拿掉就可以直接用一個 Counter 再跑一遍紀錄每個元素出現的次數。

最後，再去跑一遍 Counter 把它轉成結果需要的字串就可以通過這題了！

```py
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula += "$" # end
        stack = []
        num = []
        for c in formula:
            if c.isdigit():
                num.append(c)
            elif c.islower():
                top = stack.pop()
                top += c
                stack.append(top)
            else:
                if len(num) != 0:
                    num = int("".join(num))
                    if stack[-1] == ")":
                        tmp = []
                        stack.pop()
                        while True:
                            if stack[-1] == "(":
                                stack.pop()
                                break
                            tmp.append(stack[-1])
                            stack.pop()
                        for i in range(num):
                            stack += tmp
                    else:
                        top = stack.pop()
                        for i in range(num):
                            stack.append(top)
                    num = []
                stack.append(c)
        eleCounter = Counter(stack)
        tmp = []
        for key in sorted(eleCounter):
            if key == "$" or key == "(" or key == ")":
                continue
            tmp.append(key)
            if eleCounter[key] > 1:
                tmp.append(str(eleCounter[key]))
        return "".join(tmp)
```