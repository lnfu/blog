+++
title = 'LeetCode 60 天挑戰 D13 - Robot Collisions'
date = 2024-07-14T09:05:24Z
draft = false
tags = ['LeetCode']
+++

昨天寫完後都在用專題，結果竟然忘記記錄下來，今天補上。

連結: [2751. Robot Collisions](https://leetcode.com/problems/robot-collisions/description/)

印象中是這個月第一個 Hard 題，不過和前面幾天用到的概念蠻像的。

題目是說有一排機器人，會給你他們的位置 (position)、生命值 (health)、方向 (direction)。

如果兩個相向的機器人遇到，比較小生命值得機器人會死掉，比較大的生命值會減少 1，如果兩個都一樣就會都死掉。

然後要問你最後剩下的所有機器人的生命值，並且順序要按照一開始出現的順序 (不是位置)。

首先是先將所有機器人用它們的位置來排序。

然後，基本上我們可以把往右的機器人想成前幾天 stack 那題的左括號 `(`，往左的機器人想成是右括號 `)`，所以遇到往右的機器人就直接放進 stack 中，不過遇到往左的我們不能直接消掉，而是要用一個迴圈不斷去它和 stack 最上面的機器人的生命值。

會有三種比較結果：
1. 它比較大，那就把它的生命值減少 1，stack 最上面的刪除 (pop)，繼續和 stack 裡面的機器人比較
2. 它比較小，那就把 stack 最上面的機器人的生命值減少 1，然後中止迴圈 (紀錄它死掉)
3. 一樣大，那就把 stack 最上面的刪除，中止迴圈 (紀錄它死掉)

如果過程 stack 已經空了，但是它還活著就代表它存活下來了，所以先將它存到一個結果的陣列中。

等到所有機器人都跑完，stack 剩下的就是所有存活且往右的機器人，所以也把他們放到結果的陣列中。

最後在將結果的陣列用 id (也就是一開始出現的順序) 排序，然後回傳生命值就可以過了。

```py3
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []
        n = len(positions)
        for i in range(n):
            robot = dict()
            robot['position'] = positions[i]
            robot['health'] = healths[i]
            robot['direction'] = directions[i]
            robot['id'] = i
            robots.append(robot)
        
        robots = sorted(robots, key=lambda robot: robot['position'])
        stack = []
        survivedRobots = []
        for robot in robots:
            if robot['direction'] == 'R':
                stack.append(robot)
            else:
                dead = False
                while len(stack) != 0:
                    if stack[-1]['health'] < robot['health']:
                        stack.pop()
                        robot['health'] -= 1
                    elif stack[-1]['health'] > robot['health']:
                        stack[-1]['health'] -= 1
                        dead = True
                        break
                    else:
                        stack.pop()
                        dead = True
                        break
                if not dead:
                    survivedRobots.append(robot)
        for robot in stack:
            survivedRobots.append(robot)
        survivedRobots = sorted(survivedRobots, key=lambda robot: robot['id'])
        ans = []
        for robot in survivedRobots:
            ans.append(robot['health'])
        return ans
```
