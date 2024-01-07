# leetcode_craker
This is a project tackling Leetcode questions for tech interview. Solutions comes with python

# 1. Dynamic Programming

AKA: Recursion with Memorization 记忆化搜索 / Pruning 剪枝

Main idea: increase space complexity to reduce time complexity. 空间换时间。 Save the intermediate calculation results with memo hashmap to avoid calculating same thing for several times.

When to use DP to solve:

1. 子问题重叠性质。子问题重叠性质是指在用递归算法自顶向下对问题进行求解时，每次产生的子问题并不总是新问题，有些子问题会被重复计算多次。
2. 无后效性。即子问题的解一旦确定，就不再改变，不受在这之后、包含它的更大的问题的求解决策影响。
3. 最优子结构性质。如果问题的最优解所包含的子问题的解也是最优的，我们就称该问题具有最优子结构性质（即满足最优化原理）。

When there comes a DP problem:

1. What is the method for bruteforce searching?
2. How to do it recursively with Memorization?
3. Turn recursion into interation to get more direct view of the complexity.

Steps for solution:

1. Define the state variables
2. Define the memo array (depending on the state variables)
3. Define the initial values
4. Define the state transition functions (trickest part)

## LeetCode questions

### [Buy and Sell Stock](https://www.bilibili.com/video/BV1Lh411x7N2/?spm_id_from=333.337.search-card.all.click&vd_source=9318d4a239bca65106b4c0e0f720d724)

[121.Best time to buy and sell stock (Easy)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

[122.Best time to buy and sell stock II (Medium)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

[123.Best time to buy and sell stock III (Hard)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

[188.Best time to buy and sell stock IV (Hard)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

[309.Best time to buy and sell stock with cooldown (Medium)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

[714.Best time to buy and sell stock with transaction fee (Medium)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

### String

5.Longest palindromic substring (Medium)

72.Edit distance (Medium)

139.Word break (Medium) Tiktok

140.Word break II (Hard)

### House Robber

[198.House robber (Medium)](https://leetcode.com/problems/house-robber/)

[213.House robber II (Medium)](https://leetcode.com/problems/house-robber-ii/)

# 2. Binary Tree

## 2.1 Traversal

## 2.2 Divide and Conquer

## 2.3 Depth-first Search (DFS)

## 2.4 Breadth-first Search (BFS)

## 2.5 BFS vs. DFS

# 3. Linked List

# 4. Two Pointers

# 5. Array

