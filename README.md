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
2. Define the dp array (depending on the state variables)
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

# 2. Binary Search

> Note Reference: https://github.com/lexiewangdl/pyalgo?tab=readme-ov-file#2-binary-trees

## LeetCode Questions

# 3. DFS (Depth-First Search)

Depth-First Search (DFS) is a versatile algorithm that is commonly used to traverse or search through data structures like graphs and trees. When tackling coding questions that involve DFS, follow these general steps:

1. **Define data structures and necessary variables:**
   - Tree (comes with the problem)
   - Matrix (comes with the problem)
   - Graph (use dictionary or adjacency lists to build)
2. **Keep track of visited nodes to avoid infinite loops:**
   - Set: if we only need to track one node is visited or not (two status)
   - List: if we need to track one node is visited (1), not visited (0) and being visited in current dfs (-1) (three status)
     - e.g. find a cycle in the graph [207.Course Schedule (Medium)](https://leetcode.com/problems/course-schedule/); [210 Course Schedule II (Medium)](https://leetcode.com/problems/course-schedule-ii/description/)
   - Binary tree doesn't need visited trackoį-0p∏¸
3. **Define main function to ensure what we want our dfs do:**
   - If the input structure has multiple components (disconnected graphs or trees, diffrent grid in matrix), make sure to visit all components.
4. **Define base cases to ensure the recursion terminates correctly:**
   - Tree: reaching a leaf node.
   - Matrix: getting out of the matrix or visited
   - Graph: visited
5. **Process Current Node:**
   - Perform the necessary operations on the current node, update any relevant information or data structures.
   - (tricky) Sometimes we also need to process current node after dfs the neighbors
     - e.g. [207.Course Schedule (Medium)](https://leetcode.com/problems/course-schedule/); [210 Course Schedule II (Medium)](https://leetcode.com/problems/course-schedule-ii/description/)
6. **Explore Neighbors:**
   - Tree: visit left child and right child
   - Matrix: visit adjacent cells in for directions
   - Graph: visit nodes directed by current node
7. **Backtrack (if needed):**
   - Depending on the problem, you might need to undo certain changes made during the DFS to backtrack and explore other paths.
8. **Optimizations (if needed):**
   - Depending on the problem, you might need to optimize your solution. This could involve pruning unnecessary branches or using additional data structures.

## DFS in Binary Tree

1. Pre-order traversal / 前序遍历 = 根左右
   - 通常如果题目对遍历位置不敏感，就用前序遍历，没什么特别的。
   - 一棵二叉树的前序遍历结果 = 根节点 + 左子树的前序遍历结果 + 右子树的前序遍历结果
   - Time complexity O(N), space complexity O(h) where *h* is height of tree. If we don't consider call stack, then space complexity is O(1).
   - e.g. Quick sort
2. In-order traversal / 中序遍历 = 左根右
   - 主要用于Binary search tree (BST)
   - BST 的中序遍历结果为 *non-decreasing* order
   - Time complexity O(N), space complexity O(h) where *h* is height of tree. If we don't consider call stack, then space complexity is O(1).
   - e.g. Binary search tree
3. Post-order traversal / 后序遍历 = 左右根
   - 后续遍历十分特殊，因为 post-order operations have access to information passed up from the children (sub-trees).
   - 一旦题目和**子树**有关，大概率要给函数设置一个返回值，然后用后续遍历。
   - Use cases: e.g. merge sort, delete a node from a binary tree, subtree problems

## DFS in Graphs

## DFS in Matrix

## LeetCode Questions

### Tree

100.Same Tree (Easy)

101.Symmtric Tree (Easy)

[104.Maximum Depth of Binary Tree (Easy)](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)

236.Lowest Common Ancestor of a Binary Tree (Medium)

[1448.Count Goodd Nodes in Binary Tree (Medium)](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)

[437.Path Sum III (Medium)](https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75)

[1372.Longest ZigZag Path in a Binary Tree (Medium)](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)

### Graph

[207.Course Schedule (Medium)](https://leetcode.com/problems/course-schedule/)

[210 Course Schedule II (Medium)](https://leetcode.com/problems/course-schedule-ii/description/)

[841.Keys and Rooms (Medium)](https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75)

[547.Number of Provinces (Medium)](https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75)

[1466.Recorder Routes to Make All Paths Lead to the City Zero (Medium)](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75)

Evaluate Division (Medium)

### Matrix

[200.Number of Islands (Medium)](https://leetcode.com/problems/number-of-islands/)

[130.Surrounded Regions (Medium)](https://leetcode.com/problems/surrounded-regions/description/?envType=study-plan-v2&envId=top-interview-150)

[329.Lonegest Increasing Path in a Matrix (Hard)](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)

947.Most Stones Removed with Same Row or Column (Hard)

### Other

[365.Water and Jugs (Medium)](https://leetcode.com/problems/water-and-jug-problem/description/)

# 4. BFS (Breadth-First Search)

When to use DFS? When to use BFS?

- BFS uses O(w) extra memory, where w is the maximum width of the tree
  - Maximum width of a binary tree is 2^(h), where *h* is the height of the tree and *h* starts from 0
  - Worst case: a binary tree is a linked list, then *h* is equal to *N*
  - Height of a *balanced* tree is O(log N)
- DFS uses extra space because of the *functional call stack*, O(h) extra space.
- 如果 tree 是 balanced，那么BFS需要的extra space更多；如果 tree 是 linked list，那么DFS需要的extra space更多。
- DFS 通常都是 recursive code, use call stack, BFS 通常都是 iterative code, use queue.
- BFS starts visiting from *root*, DFS starts visiting from *leaves*. 如果你要找的target更接近于root，那么BFS更适合。

## LeetCode Questions

### Tree

Binary Tree Rigth Side View (Medium)

1161.Maximum Level Sum of a Binary Tree (Medium)

### Graph

Nearest Exit from Entraance in Maze (Medium)

Rotting Oranges (Medium)

### Other

322.Coin Change (Medium)

# 5. Linked List

# 6. Array / String

## 1. Two Pointers

## 2. Sliding Window

## 3. Prefix Sum

# 

