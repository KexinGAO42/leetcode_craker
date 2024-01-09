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

> Note Reference: https://github.com/lexiewangdl/pyalgo?tab=readme-ov-file#2-binary-trees

## 2.1 Traversal

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

## 2.2 Divide and Conquer

## LeetCode Questions

100.Same Tree (Easy)

101.Symmtric Tree (Easy)

236.Lowest Common Ancestor of a Binary Tree (Medium)

1161.Maximum Level Sum of a Binary Tree (Medium)

# 3. DFS (Depth-First Search)

Depth-First Search (DFS) is a versatile algorithm that is commonly used to traverse or search through data structures like graphs and trees. When tackling coding questions that involve DFS, follow these general steps:

1. **Choose Data Structures:**
   - Identify the appropriate data structures for your problem, such as graphs, trees, or adjacency lists.
   - Initialize any necessary variables or data structures.
2. **Visited Nodes:**
   - Maintain a data structure (e.g., a set or array) to keep track of visited nodes to avoid infinite loops.
3. **Define Base Cases:**
   - Clearly define the base cases for your recursion to ensure it terminates correctly.
   - For example, if you're traversing a tree, a common base case is reaching a leaf node.
4. **Process Current Node:**
   - Perform the necessary operations on the current node (or vertex).
   - Update any relevant information or data structures.
5. **Explore Neighbors:**
   - For each unvisited neighbor of the current node, recursively call the DFS function or push it onto the stack.
   - If using an explicit stack, continue popping and processing nodes until the stack is empty.
6. **Backtrack (if needed):**
   - Depending on the problem, you might need to undo certain changes made during the DFS to backtrack and explore other paths.
7. **Handle Multiple Components (if applicable):**
   - If the input structure has multiple components (disconnected graphs or trees), make sure to visit all components.
8. **Optimizations (if needed):**
   - Depending on the problem, you might need to optimize your solution. This could involve pruning unnecessary branches or using additional data structures.

## LeetCode Questions

[200.Number of Islands (Medium)](https://leetcode.com/problems/number-of-islands/)

329.Lonegest Increasing Path in a Matrix (Hard)

947.Most Stones Removed with Same Row or Column (Hard)

[207.Course Schedule (Medium)](https://leetcode.com/problems/course-schedule/)

210 Course Schedule II (Medium)

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

322.Coin Change (Medium)

# 5. Linked List

# 6. Two Pointers

# 7. Array

