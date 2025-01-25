# leetcode_craker
This is a project tackling Leetcode questions for tech interview. Solutions comes with python

# Algorithmic Strategies

## 1. Divide-and-Conquer

- Divide a larger problem into smaller problems that can be solved independently of each other.
- The subsolutions produced by these subproblems are then combined to grenerate the overall solution of the problem.
- Example: Apache Spark Map-Reduce.
- It's a top-down method.

## 2. Dynamic Programming

- Starting with the smallest subproblem and keep on combining the solutions, until the final solution is reached.
- Applicable when the subproblems are not independent (in contrast to Divide and Conquer).
- It's a bottom-up method.

AKA: Recursion with Memorization 记忆化搜索 / Pruning 剪枝

Main idea: increase space complexity to reduce time complexity. Save the intermediate calculation results with memo hashmap to avoid calculating same thing for several times. (Fibbonacci number is a perfect and simple example.)

Properties of DP problems:

1. Optimal Structure: 
2. Overlapping Subproblems:



When there comes a DP problem:

1. What is the method for bruteforce searching?
2. How to do it recursively with Memorization?
3. Turn recursion into interation to get more direct view of the complexity.

Steps for solution:

1. Consider edge cases (optional)

2. Define the state variables (optional)

3. Define the dp array (depending on the state variables)

   1. a single or several variants - O(1) extra space
   2. a 1D array - O(N) extra space
   3. a multi-dimensional array - O(N^2) extra space

     Note: We may always think about whether we could reduce the size of dp (if the previous solutions no longer neccesary after they have been used) 

4. Define the initial values

   1. Matrix:
      1. the top-left / bottom-right corner be the same as the original matrix
      2. the first row and column be the same as the original matrix

5. Define the state transition functions (trickest part)

### LeetCode questions

#### [Buy and Sell Stock](https://www.bilibili.com/video/BV1Lh411x7N2/?spm_id_from=333.337.search-card.all.click&vd_source=9318d4a239bca65106b4c0e0f720d724)

[121.Best time to buy and sell stock (Easy)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

[122.Best time to buy and sell stock II (Medium)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

[123.Best time to buy and sell stock III (Hard)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

[188.Best time to buy and sell stock IV (Hard)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

[309.Best time to buy and sell stock with cooldown (Medium)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

[714.Best time to buy and sell stock with transaction fee (Medium)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

#### House Robber

[198.House robber (Medium)](https://leetcode.com/problems/house-robber/)

[213.House robber II (Medium)](https://leetcode.com/problems/house-robber-ii/)

#### String

##### Multi-dimensional DP

[5.Longest palindromic substring (Medium)](https://leetcode.com/problems/longest-palindromic-substring/description/)

[72.Edit distance (Medium)](https://leetcode.com/problems/edit-distance/description/?envType=study-plan-v2&envId=leetcode-75)

[1143. Longest Common Subsequence (Medium)](https://leetcode.com/problems/longest-common-subsequence/)

[97. Interleaving String (Medium)](https://leetcode.com/problems/interleaving-string/)

[139. Word Break (Medium)](https://leetcode.com/problems/word-break/) (very tricky) Tiktok

140.Word break II (Hard)

#### Matrix (Multi-dimensional)

##### Bottom-up

[64. Minimum Path Sum (Medium)](https://leetcode.com/problems/minimum-path-sum/)

[120. Triangle  (Medium)](https://leetcode.com/problems/triangle/)

##### Top-down

[221. Maximal Square (Medium)](https://leetcode.com/problems/maximal-square/)

## 3. Greedy Algorithm
- Quickly produces a good solution, but might not be the optimal solution.
- Like DP, mainly used to solve optimization problems where divide and conquer cannot be used.
- Solution is calculated following a sequence of steps. At each step, a locally optimal choice is made.

Conditions to use Greedy Programming
1. Global from Local: A global optimum can be arrived at by selecting a local optimum.
2. Optimal substructure: An optimal solution to the problem is made from optimal solutions of sub problems.

# 2. Binary Search

When to use Binary Search:

1. In the simplest case, when we have a sorted array, and we want to find a target value in it, we can use Binary Search.
   - e.g. [374.Guess Number Higher or Lower (Easy)](https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75)
2. **In the general case**: if we can define a function (if condition) that map elements in left half to True and the other half to False or vice versa, we can use Binary Search.
   - e.g. [33.Search in Rotated Array (Medium)](https://leetcode.com/problems/search-in-rotated-sorted-array/description/); [162.Find Peak Element (Medium)](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
3. If the question ask you to search a target with logarithmic TC, it's highly possible to be a binary search question.

Steps for solving Binary Search question:

1. Initialize left and right pointers (the first index and last index of the sequence)
2. Use a while loop to continue the search until the low pointer is less than or equal to the high pointer
3. Calculate the mid point.
   - Use `mid = left + (right - left) // 2` rather than `mid = (right + left) // 2`. The latter one might cause overflow while the former one will never. For example, in C++ and Javaa, int type fits values up to around 2^31, if two such values are added, the sum will overflow.
4. Update the two pointers to find the target.

## Complexity

TC: `O(log n)`

## Pseudo Code

```python
l, r = 0, n - 1
while l <= r:
  mid = l + (r - l) // 2
  if array[mid] == target:
    return mid
  if array[mid] < target:  # the target is in the right part of the array
    l = mid + 1  # update left bound
  else:  # the target is in the left part of the array
    r = mid - 1  # update right bound
return -1
```

## LeetCode Questions

[374.Guess Number Higher or Lower (Easy)](https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75)

[33.Search in Rotated Array (Medium)](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

[162.Find Peak Element (Medium)](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

[2300.Successful Pairs of Spells and Potions (Medium)](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

[875.Koko Eating Bananas (Medium)](https://leetcode.com/problems/koko-eating-bananas/)

[4.Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Binary Search Tree (BST)

Definition of BST: In a BST, the left subtree of a node contains only nodes with keys less than the node's key, and the right subtree contains only nodes with keys greater than the node's key.

The reason we need a data structure as BST is that, to perform deletion and insertion in a sorted array requires TC of `O(n)`, whereas in BST, the operations requires TC of `O(log n)`.

#### Key operations:

1. Insertion
   
2. Deletion
   - Node with one child: Replace the node with its child.
   
   - Node with two children: find the minimum value in the right tree (keep traversing left), recursively delete the right child.
   
     [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

#### Property of the tree

[235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

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
   - Binary tree doesn't need visited track
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

[814.Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/description/)

### Graph

[207.Course Schedule (Medium)](https://leetcode.com/problems/course-schedule/)

[210 Course Schedule II (Medium)](https://leetcode.com/problems/course-schedule-ii/description/)

[841.Keys and Rooms (Medium)](https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75)

[547.Number of Provinces (Medium)](https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75)

[1466.Recorder Routes to Make All Paths Lead to the City Zero (Medium)](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75)

[399.Evaluate Division (Medium) (A bit hard actually)](https://leetcode.com/problems/evaluate-division/description/?envType=study-plan-v2&envId=leetcode-75)

### Matrix

[200.Number of Islands (Medium)](https://leetcode.com/problems/number-of-islands/)

[130.Surrounded Regions (Medium)](https://leetcode.com/problems/surrounded-regions/description/?envType=study-plan-v2&envId=top-interview-150)

[329.Lonegest Increasing Path in a Matrix (Hard)](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)

947.Most Stones Removed with Same Row or Column (Hard)

### Other

[365.Water and Jugs (Medium)](https://leetcode.com/problems/water-and-jug-problem/description/)

# 4. BFS (Breadth-First Search)

BFS algorithms start from a source node and visits all its neighbors before moving on to the next level of neighbors. BFS guarantees that it visits nodes in increasing order of their distance from the source node. BFS is often used to find the shortest path in an unweighted graph.

1. **Start from a Source Node**
2. **Enqueue the Source Node:** Add the source node to a queue (First In First Out) data structure.
   - Use the deque methods from collections
3. **Mark the Source Node as Visited**
   - Use `set()` to keep track of visited node
   - In some cases, we can directly modify the cell to mark it as visited
4. **While the Queue is Not Empty**
   - Dequeue a node from the front of the queue.
   - Visit and process the dequeued node.
   - Enqueue all unvisited neighbors of the dequeued node.
   - In some cases, we want a for loop inside the while loop so that we finish processing all node at this level
5. **Repeat Until the Queue is Empty:** Continue the process until the queue becomes empty. This ensures that all reachable nodes are visited.
6. **Check for Unvisited Nodes:** After the BFS is complete, check if there are any unvisited nodes. If yes, repeat the process for those nodes to cover the entire graph.

## Pseudo Code

```python
from collections import deque

​	def bfs(graph, start_node):    

​		# Initialize a queue for BFS   

​		queue = deque([start_node])     

​		# Mark the start node as visited

​		visited = set([start_node])

​		while queue:

​			# Dequeue a node from the front of the queue

​			current_node = queue.popleft()

​			# Process the current node (e.g., print, store, or manipulate data)

​			# Enqueue unvisited neighbors

​			for neighbor in graph[current_node]:

​				if neighbor not in visited:

​					# Mark the neighbor as visited

​					visited.add(neighbor)

​					# Enqueue the neighbor 

​					queue.append(neighbor)
```

## When to use DFS? When to use BFS?

- Space Complecity:
  - BFS uses O(w) extra space, where w is the maximum width of the tree
    - Maximum width of a binary tree is 2^(h), where *h* is the height of the tree and *h* starts from 0
    - Worst case: when a binary tree is a linked list (only one branch), then *h* is equal to *N*
    - *h* of a *balanced* tree is O(log N)
  - DFS uses O(h) extra space because of the *functional call stack*
  - If a tree is balanced, then BFS requires more space；if a tree is a linked list，then DFS needs more space
- Time Complexity: The time complexity for both DFS and BFS is essentially the same ( **O(V + E)**, where V is the number of vertices and E is the number of edges ), but the choice depends on the specific problem requirements and the nature of the graph.

- Use **DFS** when memory is a concern, and you want to explore deep into the graph.
- Use **BFS** when finding the shortest path or exploring the graph level by level is important.

## LeetCode Questions

### Tree

Binary Tree Rigth Side View (Medium)

1161.Maximum Level Sum of a Binary Tree (Medium)

### Graph

[1926. Nearest Exit from Entrance in Maze (Medium)](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

[994.Rotting Oranges (Medium)](https://leetcode.com/problems/rotting-oranges/description/?envType=study-plan-v2&envId=leetcode-75)

[286. Walls and Gates (Medium)](https://leetcode.com/problems/walls-and-gates/)

[934. Shortest Bridge](https://leetcode.com/problems/shortest-bridge/)

1293.Shortest Path in a Grid with Obstacles Elimination (Hard)

### Other

[127.Word Ladder (Hard) Tiktok](https://leetcode.com/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150)

[322.Coin Change (Medium)]([322. Coin Change](https://leetcode.com/problems/coin-change/))

# 5. Linked List

## Code template

1. Basic operations: insertion, deletion, traversal

```python
# Insert node c (head -> b, head -> c -> b)
c.next = head.next
head.next = c

# Delete node c (head -> c -> b, head -> b)
head.next = head.next.next

# Traverse linked list
while head:
  head = head.next
```

2. Reverse linked list

```python
curr = head
prev = None
while curr:
  nxt = curr.next
  curr.next = prev
  prev = curr
  curr = nxt
```

3. Dummy head

```python
dummy.next = head
while head:
  # operations of delete, insert...
  head = head.next
return dummy.head
```

4. Slow and fast pointers

This method is usually used in problems which require: a) finding a middle node in a linked list; b) detecting a cycle in a linked list

## LeetCode Questions

### Reverse Linked List

[25. Reverse Nodes in k-Group (Hard)](https://leetcode.com/problems/reverse-nodes-in-k-group/)

### Slow and Fast Pointers

[2095. Delete the Middle Node of a Linked List (Medium)](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

[142. Linked List Cycle II (Medium)](https://leetcode.com/problems/linked-list-cycle-ii/)

# 6. Array / String

## 1. Two Pointers

Why do we want to use Two Pointers:

When we want to search for two elements from an array, the brute force solution could lead to nested loops. Two pointers can often solve problems in linear or linearithmic time.

Types of Two Pointers:

1. Left and right pointers: the pointers are initialized at the beginning and the end of the array; both pointers move towards the middle

   - In this case, we don't care about the elments between the two pointers

   Code template:

   ```python
   def template(array):
   	left, right = 0, len(array) - 1
     
     while left < right:
       if ...:
          left += 1
       if ...:
          right -= 1
   ```

2. Slow and fast pointers: the pointers are initialized at the beginning of the array; the fast pointer moves along the array by for loop, while the slow pointer moves only under certain conditions; for each loop, check the subarray [slow : fast] to see whether it meets certain condition

   - In this case, we DO care about the elments between the two pointers
   - Subtypes:
     - Remove duplicates
     - Sliding Window

   

### LeetCode Questions

#### Left and right pointers

[11. Container With Most Water (Medium)](https://leetcode.com/problems/container-with-most-water/)

[581. Shortest Continuos Unsorted Subarray (Medium)](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/) => Monotonic stack

#### Slow and fast pointers

#### Move pointers conditionally

[1868. Product of Two Run-Length Encoded Array](https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/description/)

## 2. Sliding Window

Common scenarios for using Sliding Window: finding the maximum/minimum subarray, longest substring with distinct characters, or a subarray with a given sum.

Common constraints: some problems have specific conditions or restrictions on the **window size** or **elements inside the window**.

How to Slide the Window:

Set up variables to represent the window **(left and right pointers)** and any other necessary information.

- every SW problem needs left and right pointers to represent the window
- if the window size is fixed as `k`:
  - `left, right = 0, k - 1` (use `for i in range(k)` to traverse the first window)
  - for sliding the window, use `for i in range(k, len(arr))`, where `left, right = i - k, i`
- if the window size is not fixed, and the constraints are on the elements inside the window:
  - `left, right = 0, 0`
  - `for right in range(len(arr))`, update left according to the constraint

### LeetCode Questions

##### Fixed window size

[456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

##### Other constraints

[1004. Max Consecutive Ones III (Medium)](https://leetcode.com/problems/max-consecutive-ones-iii/) Similar question: [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

[76. Minimum Window Substring (Hard)](https://leetcode.com/problems/minimum-window-substring/)

## 3. Prefix Sum

When to use Prefix Sum:

1. Subarray Sum or Range Queries:
   - If the problem involves finding the sum of elements in a subarray or handling range queries (queries about subarray sums), prefix sum is often a good choice. It allows you to calculate subarray sums efficiently.
2. Cumulative Operations:
   - If the problem involves cumulative operations on an array, such as finding the running sum or cumulative frequency, prefix sum can simplify and optimize these calculations.
3. Optimizing Time Complexity:
   - If the problem can be solved with a time complexity of O(N) or better using prefix sum, it might be a suitable approach. Prefix sum allows you to perform certain calculations in constant time, improving overall efficiency.
4. Reduction to a Known Problem:
   - If the problem can be reduced to a known problem that involves subarray sums or cumulative operations, consider using prefix sum as a tool to solve the problem efficiently.
5. Avoiding Repeated Calculations:
   - If there are repeated calculations of cumulative sums or subarray sums, using a prefix sum array can help avoid redundant computations and improve performance.
6. Requirements Involving Differences:
   - If the problem involves finding the difference between two subarray sums or handling queries related to differences between elements, prefix sum can be useful.

Complexity:

TC: `O(N)`

SC: `O(N)` when we need an array to store the prefix sums / `O(1)` when we only need a running sum

### LeetCode Questions

[560. Subarray Sum Equals K (Medium)](https://leetcode.com/problems/subarray-sum-equals-k/) (Combine with Sliding Window)

[2483. Minimum Penalty for a Shop (Medium)](https://leetcode.com/problems/minimum-penalty-for-a-shop/)

[1658. Minimum Operations to Reduce X to Zero (Medium)](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/) (Combine with two sums)



# 7. Queue / Stack

## 1. Heap / Priority Queue

## 2. Monotonic Stack
