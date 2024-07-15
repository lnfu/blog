+++
title = 'LeetCode 60 天挑戰 D15 - Create Binary Tree From Descriptions'
date = 2024-07-16T00:19:14+08:00
draft = false
tags = ['LeetCode']
+++

今天第 15 天，白天實習都在寫我最討厭的測試，晚上專題又有點卡關，然後我的環境好像又有問題，決定星期四回新竹直接把機器重灌順便整理一下思緒...

總而言之，今天心情不太好，感覺很多事情都還沒做完...

連結: [2196. Create Binary Tree From Descriptions](https://leetcode.com/problems/create-binary-tree-from-descriptions/description/)

今天題目蠻簡單的，我白天的時候抽空就把它解了。

題目大意是說給定一連串關於二元樹 parent/child 的 pair，並且會告訴你 child 是左子樹還是右子樹。

然後你要建出這個二元樹並且回傳他的根節點。

基本上就跑過一遍然後對把每次遇到的 parent/child 連起來就好了，不過我用了一個 map 來記錄節點，如果不存在 map 就需要初始化一個節點 (題目有說每個節點的值會保證不相同，所以用值當作 key 就可以了)。

```py3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        store = dict()
        childSet = set()
        parentSet = set()
        for parentVal, childVal, isLeft in descriptions:
            childSet.add(childVal)
            parentSet.add(parentVal)
            if parentVal not in store:
                store[parentVal] = TreeNode(parentVal)
            if childVal not in store:
                store[childVal] = TreeNode(childVal)

            if isLeft:
                store[parentVal].left = store[childVal]
            else:
                store[parentVal].right = store[childVal]
        return store[parentSet.difference(childSet).pop()]
```
