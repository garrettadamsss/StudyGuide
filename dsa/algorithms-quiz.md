# Algorithms Quiz

Based on [algorithms.md](./algorithms.md). Work through each section without peeking at the answer key.

---

## Part 1 — Sorting & Binary Search

**1.** What is the main difference between Python’s `list.sort()` and `sorted()`?

- A) `sort()` returns a new list; `sorted()` modifies in place  
- B) `sort()` modifies in place and only works on lists; `sorted()` returns a new list and accepts any iterable  
- C) Both always return a new list  
- D) `sorted()` only works on tuples  

**2.** Merge sort has two high-level phases. Name them in order.

**3.** In the merge step of merge sort, when `left[i]` and `right[j]` are equal, which side does the doc’s implementation take first?

**4.** Binary search requires the input to be ___ before you search.

**5.** During binary search, if `target > numbers[mid]`, which index do you update and how?

- A) `right = mid - 1`  
- B) `left = mid + 1`  
- C) `left = mid - 1`  
- D) `right = mid + 1`  

**6.** True or false: The loop condition for binary search in the doc is `while left < right`.

---

## Part 2 — Hashing

**7.** Fill in the flow from the doc: Key → ___ → Index → Value

**8.** What formula does the doc use to map a key to a table index?

**9.** HashMap vs HashSet — which stores key–value pairs, and which stores unique values only?

**10.** Which problem signal best fits hashing? (Choose all that apply.)

- A) Count how many times each element appears  
- B) Quickly check whether you’ve seen a value before  
- C) Find the shortest path in an unweighted graph level by level  
- D) Associate one piece of data with another  

---

## Part 3 — Recursion

**11.** List three problem-pattern signals from the doc that suggest recursion.

**12.** In the recursion checklist, what is the base case for?

**13.** For Fibonacci in the doc, what does `fib(0)` return and what does `fib(1)` return?

**14.** True or false: The doc recommends visualizing recursion as a tree where each node is a subproblem.

---

## Part 4 — Two Pointers

**15.** What time-complexity improvement is two pointers often trying to achieve compared to nested loops?

**16.** Match the pointer setup to the typical use case:

| Setup | Use case |
| ----- | -------- |
| 1. Opposite ends, move inward | |
| 2. Same direction (slow/fast) | |
| 3. One pointer per sequence | |

Options (use each once): **sorted pair / target sum**, **remove duplicates / partition**, **merge two sorted arrays**

**17.** For a sorted array and “find two numbers that sum to target,” why can opposite-direction pointers eliminate candidates safely?

**18.** In the doc’s `removeDuplicates`, what does pointer `l` represent and what does `r` do?

---

## Part 5 — Sliding Window

**19.** Complete the distinction from the doc:

- Two pointers = two positions that move according to some rule.  
- Sliding window = two pointers defining a continuously maintained ___.

**20.** Fixed-size vs dynamic window — which one grows/shrinks the window based on a validity condition?

**21.** Which keywords in a problem statement suggest sliding window? (Choose all that apply.)

- A) “contiguous”  
- B) “subarray”  
- C) “permutation”  
- D) “without repeating characters”  
- E) “longest substring”  

**22.** In a fixed window of size `k`, after the initial sum, how does the doc update the window sum when sliding one step right?

---

## Part 6 — Greedy

**23.** Name the two structural properties that define a greedy problem in the doc.

**24.** Why does the doc warn you to verify greedy with a counterexample before relying on it?

**25.** For **Assign Cookies**, what is the greedy choice after sorting children and cookies?

**26.** For **Non-Overlapping Intervals**, why sort by end time (`a[1]`), and what happens when `intervals[l][1] > intervals[r][0]`?

**27.** Coins `[1, 3, 4, 5]`, amount `7`: greedy (largest first) uses how many coins? The optimal (DP-style) answer uses how many?

---

## Part 7 — Dynamic Programming

**28.** Why does naive recursive Fibonacci blow up to roughly `O(2^n)`?

**29.** Top-down DP (memoization) vs bottom-up (tabulation) — which starts from the original problem and caches recursive results, and which fills a table from smallest subproblems upward?

**30.** For coin change, write the meaning of state `dp[a]` and the base case `dp[0]` from the doc’s template.

**31.** Write the recurrence shape from the doc: `dp[a] = ___`

**32.** List four “problem clues” from the doc that point toward DP.

**33.** Greedy vs DP (same table in the doc): Greedy decides by ___; DP tries ___ and keeps the best overall using stored subproblem answers.

---

## Part 8 — Backtracking

**34.** What three steps form the backtracking loop after making a choice?

**35.** Backtracking explores possibilities using which graph traversal idea?

**36.** Fill in the table:

| Type | Order matters? | Typical constraint |
| ---- | -------------- | ------------------ |
| Permutation | | |
| Combination | | fixed size *k* |
| Subset | | any size 0…*n* |

**37.** For distinct items with no repeats, how many **subsets** does a set of size *n* have? (Use the doc’s formula.)

**38.** True or false: In backtracking, you undo a choice so you can try the next option on the same partial state.

---

## Part 9 — Trees (BFS & DFS)

**39.** Which data structure does tree BFS use, and in what order does it visit nodes?

**40.** Tree BFS is a good fit when the problem involves ___ path or ___ by level. (Name two themes from the doc.)

**41.** Name the three DFS traversal orders and where the current node is processed in each (relative to left and right children).

**42.** Which traversal order is natural for “values from a BST in sorted order” (standard CS fact — connect to inorder in the doc)?

**43.** For **max depth**, what does each recursive call return at a null node, and how does a parent combine left and right results?

**44.** For **hasPathSum**, at what kind of node do you compare `currentSum` to `targetSum`?

---

## Part 10 — Graphs

**45.** What is the biggest implementation difference between graphs and trees in the doc?

**46.** Graph BFS uses a ___; graph DFS is associated with a ___ (conceptually).

**47.** When should you prefer BFS on a graph according to the problem clues? Name two situations.

**48.** When should you prefer DFS on a graph? Name two themes from the doc (e.g., cycles, regions).

**49.** In the doc’s graph BFS, when do you mark a neighbor as visited — when you enqueue it or when you dequeue it?

---

## Part 11 — Pattern recognition (mixed)

For each scenario, name the **primary** technique from the doc (be specific: e.g. “dynamic sliding window,” not just “two pointers”).

**50.** Sorted array, find two indices whose values sum to `target` with `O(1)` extra space.

**51.** String: longest contiguous substring with all unique characters.

**52.** Generate every subset of `{A, B, C}`.

**53.** Unweighted graph: minimum number of edges from `start` to `goal`.

**54.** Coin denominations unlimited; minimize number of coins for amount `n` (global optimum required).

**55.** Interval list: maximize count of non-overlapping intervals (minimum removals).

**56.** Binary tree: return nodes level by level, left to right within each level.

---

## Part 12 — Quick fire

**57.** Merge sort: stable or not? (Doc doesn’t say — answer from the merge rule you studied in Q3.)

**58.** Hash lookup/insert/delete: what complexity class does the doc imply when hashing works well?

**59.** Kadane’s algorithm appears under which section header in the doc? (What topic is it grouped with?)

**60.** Dijkstra’s algorithm — what does the doc file list it under, and what kind of graph problem is Dijkstra typically used for? (Brief answer; section is mostly a stub in the doc.)

---

# Answer Key

<details>
<summary>Click to reveal answers</summary>

### Part 1
1. **B**  
2. **Divide** (split in half recursively), then **Conquer/Merge** (merge sorted halves).  
3. **Left** (`left[i]` when `left[i] <= right[j]`).  
4. **Sorted** (ascending).  
5. **B** — `left = mid + 1`.  
6. **False** — doc uses `while left <= right`.

### Part 2
7. **Hash function** (hash function → index).  
8. `index = hash(key) % tableSize`  
9. **HashMap** = key–value; **HashSet** = unique values only.  
10. **A, B, D** (C is BFS on graphs).

### Part 3
11. Any three: solve smaller version of same problem; tree → DFS/recursion; nested structure of unknown depth; explore all possibilities.  
12. **Stopping condition** — when the call can answer immediately without recursing further.  
13. **0** and **1**.  
14. **True**

### Part 4
15. **`O(n²)` → `O(n)`** (avoid revisiting elements).  
16. Opposite → **sorted pair/target sum**; same direction → **remove duplicates/partition**; one per sequence → **merge sorted arrays**.  
17. Because the array is sorted, if the sum is too large/small, moving the left/right pointer can’t discard a valid pair that would still be reachable with the other pointer.  
18. **`l`** is the position of the last unique element kept; **`r`** scans ahead and copies new unique values forward.

### Part 5
19. **Range** (continuous sub-range).  
20. **Dynamic (variable-size)** window.  
21. **A, B, D, E**  
22. `window_sum = window_sum - nums[i - k] + nums[i]` (drop left of window, add new right).

### Part 6
23. **Greedy choice property** and **optimal substructure**.  
24. Local best choices don’t always yield a global optimum (coin change example).  
25. Smallest cookie that still satisfies the current smallest unsatisfied child (both sorted ascending).  
26. Sort by end time to keep intervals that finish earliest; overlap means current end extends past next start → increment removal count (greedy keep earlier-finishing interval).  
27. Greedy: **3** (5+1+1); optimal: **2** (3+4).

### Part 7
28. **Overlapping subproblems** — same `fib(k)` computed many times in the recursion tree.  
29. **Top-down** = original problem + cache; **bottom-up** = tabulation from base cases.  
30. `dp[a]` = minimum coins to make amount `a`; `dp[0] = 0`.  
31. `min(dp[a - coin] + 1)` over valid coins (doc shorthand).  
32. Any four: min/max/longest/shortest among choices; count ways; target sum possible; capacity/knapsack-style; decision at each position; answer depends on previous positions.  
33. **Best-looking option now** vs **every valid choice** (with `dp[...]`).

### Part 8
34. **Explore** (recurse), then **undo/backtrack** the choice (third step in “choose → explore → undo”).  
35. **DFS**  
36. Permutation: **yes**; Combination: **no**; Subset: **no**.  
37. **`2^n`**  
38. **True**

### Part 9
39. **Queue**; level order (siblings before going deeper).  
40. **Shortest** path (in trees), **minimum depth / level-by-level / nearest by level** (any two from doc clues).  
41. **Preorder** — node, left, right; **Inorder** — left, node, right; **Postorder** — left, right, node.  
42. **Inorder**  
43. Null → **0**; parent returns **`max(leftMax, rightMax) + 1`**.  
44. A **leaf** (`left` and `right` both null).

### Part 10
45. Graphs need a **`visited` set** to avoid cycles/revisiting nodes.  
46. **Queue** / **Stack** (recursion).  
47. Any two: shortest path in **unweighted** graph, minimum steps/moves, explore by distance/level, closest reachable target.  
48. Any two: entire connected **region**, explore paths/choices, **cycle detection** / topological order, traverse and **backtrack**.  
49. When **enqueued** (before/at append to queue, with `visited.add`).

### Part 11
50. **Two pointers** (opposite directions on sorted array).  
51. **Sliding window** (dynamic; shrink while invalid).  
52. **Backtracking** (subsets).  
53. **BFS** (unweighted shortest path).  
54. **Dynamic programming** (coin change).  
55. **Greedy** (+ two pointers after sort by end time).  
56. **BFS** (level order).

### Part 12
57. **Stable** — equal elements taken from left first in merge.  
58. **O(1)** average (typical hash table).  
59. Under **DP Algorithms** / **Kadane’s** (maximum subarray DP).  
60. Listed under **Graph Algorithms → Dijkstra’s**; typically **shortest paths in weighted graphs** with non-negative edge weights.

</details>
