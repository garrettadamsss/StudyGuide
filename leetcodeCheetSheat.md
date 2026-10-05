# LeetCode Problem-Solving Framework

## Problem Clues → Patterns

| Problem Clue                     | Think About                  |
| -------------------------------- | ---------------------------- |
| Need fast lookup                 | Hash Map / Set               |
| Sorted array                     | Two Pointers / Binary Search |
| Subarray / substring             | Sliding Window / Prefix Sum  |
| "Next greater"                   | Monotonic Stack              |
| Tree traversal                   | DFS / BFS                    |
| Shortest path                    | BFS / Dijkstra               |
| Connected components             | DFS / BFS / Union-Find       |
| Top K                            | Heap                         |
| Repeated overlapping subproblems | Dynamic Programming          |
| Explore all combinations         | Backtracking                 |
| Intervals                        | Sort + Greedy                |
| Linked list manipulation         | Fast / Slow Pointers         |
| Dependencies                     | Topological Sort             |
| Optimization over choices        | DP / Greedy                  |

---

# Problem-Solving Process

## 1. Understand the Problem — 2–5 min

### Write down the problem in your own words

Ask yourself:

* What are the inputs?
* What is the output?
* Can I modify the input?
* Are duplicates allowed?
* Is the input sorted?
* What are the constraints?
* Are there edge cases I should consider?

### Clarify the problem

If you're in an interview, ask questions when something is ambiguous.

### Restate the problem

Explain the problem back to yourself/interviewer in your own words.

> "Given X, I need to return Y while satisfying Z."

---

## 2. Start With Brute Force — 2–5 min

First, think of the simplest correct solution.

Ask:

* What is the most straightforward way to solve this?
* What is the time complexity?
* What makes this solution slow?

The brute-force solution gives you:

1. A correct baseline.
2. An understanding of the problem.
3. A starting point for finding an optimization.

> **Don't immediately jump to the optimal solution.**

---

## 3. Identify the Pattern — 3–5 min

Determine which data structure or algorithm naturally reduces the complexity.

Ask:

* What is the bottleneck in my brute-force solution?
* What operation needs to become faster?
* Is there a known pattern that addresses this?

Use the **Problem Clues → Patterns** chart as a reference.

Examples:

* Need `O(1)` lookup → **Hash Map / Set**
* Sorted input → **Binary Search / Two Pointers**
* Contiguous range → **Sliding Window / Prefix Sum**
* Tree traversal → **DFS / BFS**
* Top K elements → **Heap**
* All possible combinations → **Backtracking**

---

## 4. State the Invariant — 2–4 min

An **invariant** is a condition that remains true throughout an algorithm.

Think of it as a statement about what your variables or data structures **always mean**.

Ask:

1. **What must remain true?**
2. **How do I maintain that truth?**
3. **What does each variable/data structure represent?**
4. **Does every operation preserve the invariant?**

### Example: Binary Search

Invariant:

> **The target, if it exists, must be somewhere between `left` and `right`.**

Every iteration:

1. Check the middle element.
2. Eliminate half of the search space.
3. Update `left` or `right`.
4. Maintain the invariant that the target must still be within the remaining search space.

The invariant helps you u
