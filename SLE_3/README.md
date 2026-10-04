# Factory-Floor Search System (BFS vs DFS): SLE-3 Architecture

**Course:** 02AML204 – Introduction to Artificial Intelligence
**Name:** Sanskar Gorave | **PRN:** 25UAM126 | **Division:** B

## About

This project models a 6×6 textile factory floor as a grid and searches it with two uninformed search algorithms, Breadth-First Search (BFS) and Depth-First Search (DFS), to reach the Quality Inspection Station. For each algorithm it prints the number of nodes explored and times the search over 10,000 repeated runs.

SLE-3 documents the architecture of this system using the full C4 model (Context, Container, Component, Code). It builds on the same system used in SLE-1 (code) and SLE-2 (performance profiling).

## The factory grid

| Symbol | Meaning |
|---|---|
| `S` | Start |
| `G` | Goal (Quality Inspection Station) |
| `#` | Obstacle |
| `.` | Free floor |

The grid is hardcoded at the top of `factory_search.py`. To try a different layout, edit the `factory` list.

## How to run

Requires Python 3. It uses only the standard library (`collections` and `time`), so nothing needs to be installed.

```bash
python factory_search.py
```

The program prints the grid, then the nodes explored by each search, then three timing runs for each search:

```
BFS nodes explored: 22
DFS nodes explored: 17
```

The timing lines (milliseconds for 10,000 runs) depend on your machine, so your numbers will differ from the ones below.

## Results from SLE-2

Per 10,000 searches, averaged over 3 runs:

| Algorithm | Nodes explored | Average time |
|---|---|---|
| BFS | 22 | 226.39 ms |
| DFS | 17 | 141.38 ms |

## Architecture (C4 model)

| Level | What it shows | Image |
|---|---|---|
| 1. Context | The system, the user, and the py-spy profiler | `diagrams/context_diagram.png` |
| 2. Container | Input Module, Search Engine, Memory / Visited Set, Benchmark / Timing Module, Output Module | `diagrams/container_diagram.png` |
| 3. Component | Inside the Search Engine: Start Locator, Frontier, Node Counter, Goal Test, Neighbour Expander | `diagrams/component_diagram.png` |
| 4. Code | `factory`, `bfs(factory)`, `dfs(factory)` and the timing loops | see the report |

BFS and DFS share the same structure. The only real difference is the frontier: a `deque` (FIFO queue) in BFS and a list used as a stack (LIFO) in DFS.

## Repository contents

```
factory_search.py                  # BFS and DFS search, plus timing loops
diagrams/                          # C4 diagrams (PNG exports and editable .drawio files)
SLE3_25UAM126_SanskarGorave.docx   # SLE-3 report
AI_CONTRIBUTION_LOG.md             # Which parts were done with AI help
README.md
```

Move the exported diagram PNGs and `.drawio` files into the `diagrams/` folder, and rename them to match the paths in the table above, so the links work.

## Limitations

- The grid is hardcoded; there is no input prompt or file loading.
- The searches return only the number of nodes explored, not the path to the goal.
- There is no A* search or heuristic.

## AI use

ChatGPT and Claude were used for this work. See [`AI_CONTRIBUTION_LOG.md`](AI_CONTRIBUTION_LOG.md) for what AI did and what I did myself.
