# SLE-2: BFS vs DFS Performance Comparison

## Course
**02AML204 – Introduction to Artificial Intelligence**

## Student
**Sanskar Gorave**
**PRN:** 25UAM126
**Division:** B

---

## 1. Project Overview

This project compares the performance of **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** for finding a Quality Inspection Station on a textile factory floor.

The factory floor is represented as a grid:

- `S` = Main Control Room (Start)
- `G` = Quality Inspection Station (Goal)
- `.` = Walkable area
- `#` = Blocked or restricted area

Both algorithms use the **same factory-floor layout** so that their performance can be compared fairly.

---

## 2. Factory-Floor Layout

```text
        1   2   3   4   5   6
      +---+---+---+---+---+---+
 A    | S |   | # |   |   |   |
      +---+---+---+---+---+---+
 B    |   |   | # |   | # |   |
      +---+---+---+---+---+---+
 C    | # |   |   |   | # |   |
      +---+---+---+---+---+---+
 D    |   | # |   | # |   |   |
      +---+---+---+---+---+---+
 E    |   |   |   | # |   |   |
      +---+---+---+---+---+---+
 F    |   | # |   |   |   | G |
      +---+---+---+---+---+---+
```

---

## 3. Algorithms Compared

| | Algorithm A | Algorithm B |
|---|---|---|
| Name | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| Frontier structure | Queue (FIFO) | Stack / recursion (LIFO) |
| Path guarantee | Shortest path in an unweighted grid | Any valid path, not necessarily shortest |

Both algorithms explore the same four moves (up, down, left, right) in the same
order and run on the identical layout shown above.

---

## 4. Profiling Method

- **Tools:** `py-spy` for flame graphs, `time.perf_counter()` for timing.
- **Runs:** 3 independent runs per algorithm.
- **Workload per run:** the search was repeated **10,000 times**, so the measured
  time is comfortably above the timer's resolution rather than sub-millisecond noise.
- **Nodes explored:** counted inside the search loop each time a node is expanded.

---

## 5. Results

| Metric | BFS | DFS | Better? |
|---|---:|---:|:---:|
| Run 1 Time (ms / 10,000 runs) | 285.9454 | 145.2534 | DFS |
| Run 2 Time (ms / 10,000 runs) | 207.8587 | 142.8757 | DFS |
| Run 3 Time (ms / 10,000 runs) | 185.3564 | 136.0209 | DFS |
| **Average Time (ms / 10,000 runs)** | **226.3868** | **141.3833** | **DFS** |
| Nodes Expanded / Explored | 22 | 17 | DFS |

### Observation

On this particular factory-floor layout, DFS had a lower average execution time
and explored fewer nodes than BFS. The timing was measured over 10,000 searches
per run to obtain a clearly measurable workload. The result is specific to this
input layout and traversal order and does not mean DFS will always be faster —
a different goal position or layout can reverse the outcome, and BFS still
guarantees the shortest path while DFS does not.

---

## 6. How to Run

```bash
# run the comparison and print timings + node counts
python factory_search.py

# generate the flame graphs
py-spy record -o bfs_profile.svg -- python factory_search.py
py-spy record -o dfs_profile.svg -- python factory_search.py
```

---

## 7. Files in This Repository

| File | Description |
|---|---|
| `factory_search.py` | Runs BFS and DFS on the same layout and reports timings and node counts |
| `bfs_profile.svg` | py-spy flame graph for BFS |
| `dfs_profile.svg` | py-spy flame graph for DFS |
| `AI_Contribution_Log.md` | Record of where AI assistance was and was not used |
| `SLE2_25UAM126_SanskarGorave.docx` | Final SLE-2 profiling report |

---

## 8. AI Contribution

AI assistance was used for understanding the requirements, structuring the code
and documentation, and interpreting the profiling output. All program execution,
profiling, timing measurement, and result verification were done by me. Full
details are in `AI_Contribution_Log.md`.
