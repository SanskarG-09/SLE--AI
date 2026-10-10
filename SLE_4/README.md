# 🏭 Factory-Floor Search System – SLE-4 (Final Viva & ADR)

**Course:** 02AML204 – Introduction to Artificial Intelligence
**Name:** Sanskar Gorave | **PRN:** 25UAM126 | **Division:** B

## 📌 Project Description

This submission documents one design decision from my Factory-Floor Search System: the use of a **visited set** and **algorithm-specific frontier data structures** in Breadth-First Search (BFS) and Depth-First Search (DFS).

The system searches a 6×6 textile factory grid from the start `S` (Main Control Room) to the goal `G` (Quality Inspection Station), avoiding blocked `#` cells and moving up, down, left or right. For each algorithm it prints the number of nodes explored and measures running time over 10,000 repeated searches.

## 🧾 Architecture Decision Record (Summary)

**Decision:** BFS uses a FIFO queue (`collections.deque`), DFS uses a LIFO stack (a Python list), and both use a visited set of (row, col) cells on the same grid.

**Alternatives considered:**
* No visited set
* A plain list for both searches
* Recursive DFS instead of an explicit stack

**Evidence from SLE-2:**

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1, ms per 10,000 searches | 285.9454 | 145.2534 |
| Run 2, ms per 10,000 searches | 207.8587 | 142.8757 |
| Run 3, ms per 10,000 searches | 185.3564 | 136.0209 |
| Average, ms per 10,000 searches | 226.3868 | 141.3833 |
| Nodes explored | 22 | 17 |

DFS was faster and explored fewer nodes on this grid and traversal order only. This does not mean DFS is always faster. BFS keeps the advantage of finding a shortest path in an unweighted grid, which DFS does not guarantee. The code returns only the node count, so path length was not measured.

**Link to SLE-3:** the Search Engine uses a Frontier and a Visited Set, and the code-level overview includes the `bfs()` and `dfs()` functions.

The full ADR is in `SLE4_25UAM126_SanskarGorave.docx`.

## 🗺️ My SLE Journey

| SLE | Work |
|---|---|
| SLE-1 | NexaBot AI, a simple rule-based Python chatbot (a separate project) |
| SLE-2 | BFS vs DFS profiling on the factory grid using `py-spy` and `perf_counter()` |
| SLE-3 | Full C4 architecture: Context, Container, Component and Code Level |
| SLE-4 | ADR on the visited set and queue/stack frontiers, with this README and the contribution log |

## 📂 Files for SLE-4

```text
├── SLE4_25UAM126_SanskarGorave.docx   (ADR submission)
├── factory_search.py                  (BFS and DFS implementation)
├── contribution_log.md                (AI contribution log)
└── README.md
```

## ▶️ How to Run

Make sure Python 3 is installed, then run:

```bash
python factory_search.py
```

The program prints the grid, then `BFS nodes explored: 22` and `DFS nodes explored: 17`, followed by the timing runs (3 runs of 10,000 searches for each algorithm). The timing results will differ slightly on each machine.

## 🤖 AI-Assisted Development

Claude was used to help draft and check the SLE-4 document, this README and the contribution log. My earlier reports list ChatGPT (SLE-2) and ChatGPT and Claude (SLE-3).

The decision, the SLE-2 and SLE-3 evidence and the code come from my own project. The AI-generated text was reviewed and shortened by me. See `contribution_log.md` for details.

## 🚀 Future Improvements

* Return the actual path found so path length can be compared
* Test larger and different grids
* Try A* with a heuristic

## 👨‍💻 Project

**Factory-Floor Search System (BFS vs DFS) – SLE-4 ADR**

GitHub: https://github.com/SanskarG-09/SLE--AI.git
