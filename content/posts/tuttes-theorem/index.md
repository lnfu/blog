+++
title = "Tutte's Theorem"
date = 2024-10-18T18:45:21+08:00
draft = false
+++

這個算是在圖論蠻重要的定理了

我還是先簡單介紹一下一些名詞定義: 奇分支 (odd component), 完美匹配 (perfect matching), 1-factor

## Odd Component

## Perfect Matching

## 1-factor

## 生成子圖 (Spanning Graph)

## 定理內容

G 有完美匹配的充分必要條件是對於所有 S 為 V(G) 的真子集 (真子集意思是 S 為 V(G) 的子集且不是 V(G))

o(G - S) 也就是 (G - S) 的 odd component 數量 <= |S|

## 證明必要性 (🠲)

假設 G 存在完美匹配 M, 對所有 S 為 V(G) 的真子集我們可以分成兩個情況討論

### G - S 沒有 odd component

此時 o(G - S) = 0, 結論必定成立

### G - S 存在 odd component

假設 A1, A2, A3, ..., Ak 是 G - S 的「所有」 odd component

每個 odd component 的點數都是奇數 (odd component 定義), 所以對於所有 odd component, 完美匹配一定會有邊的其中一個端點在這個 odd component, 另一個端點在 S (注意 odd component 一定是刪除 S 後才出現的, 不可能一開始就有, 否則不會有完美匹配)

我們可以假設對於 Ai odd component 裡面有頂點 ui 和 S 中的 vi 匹配 (i = 1, 2, 3, ..., k)

並且 vi 各自都不相同 (否則就不是匹配了)

因此我們可以得到 o(G - S) = k <= |S|

## 證明充分性 (🠰) - 使用矛盾證明

假設 G 滿足對所有的 S 為 V(G) 的真子集, o(G - S) <= |S|, 並且 G 沒有完美匹配

我們可以取 S = {}, 此時 |S| = 0, 因此 o(G) = o(G - S) 也只能是 0, 所以 G 沒有任何 odd component, 也就是所有分支的點數都是偶數, 全部加起來得到 |V(G)| 也是偶數

一個偶數的完全圖, 一定有完美匹配

如果我們持續給 G 加入原本沒有的邊, 有一天 G 就會變成完全圖, 也就有完美匹配

所以再建立這個完全圖的過程一定會有一刻是加了邊後從沒有完美匹配變成有完美匹配的圖, 我們就稱這個還沒有完美匹配的圖為 G*

顯然 G 是 G* 的生成子圖 (spanning graph)

對所有 S 屬於 V(G) 的真子集, G - S 也是 G* - S 的生成子圖

所以 o(G* - S) <= o(G - S) <= |S| (可以想成加上更多邊只能讓奇分支數變少, 不可能變多)

