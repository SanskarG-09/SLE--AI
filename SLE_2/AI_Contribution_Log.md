# AI Contribution Log

## Project
SLE-2: Performance Comparison of BFS and DFS

## Course
02AML204 – Introduction to Artificial Intelligence

## Student
Sanskar Gorave

## PRN
25UAM126

## AI Tool Used
ChatGPT

## Purpose of AI Assistance
AI assistance was used to understand the SLE-2 requirements, plan the experiment, improve the structure of the Python code, understand profiling tools, and prepare the documentation.

## Work Done with AI Assistance

1. Discussed the SLE-2 requirements and selected BFS and DFS for performance comparison.
2. Used a textile factory-floor search problem as the application scenario.
3. Used AI assistance to understand how to count nodes explored by BFS and DFS.
4. Learned how to use `py-spy` for profiling and flame-graph generation.
5. Used `time.perf_counter()` to measure execution time over multiple runs, repeating each search 10,000 times per run.
6. Used AI assistance to understand and organize the profiling results into a comparison table.
7. Used AI assistance to structure the SLE-2 report and README documentation.

## Work Done by Me

- Created and ran the Python program in VS Code.
- Prepared the factory-floor layout used for the experiment.
- Installed and used `py-spy`.
- Ran BFS and DFS on the same test problem.
- Generated the profiling files and flame graphs.
- Performed the timing experiment using `perf_counter`.
- Recorded and verified the actual execution-time results.
- Compared the number of nodes explored by both algorithms.
- Prepared the final project files and GitHub repository.

## Experimental Results

Each timing run repeated the search **10,000 times** so that the measured
workload was large enough to time reliably.

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms / 10,000 runs) | 285.9454 | 145.2534 |
| Run 2 Time (ms / 10,000 runs) | 207.8587 | 142.8757 |
| Run 3 Time (ms / 10,000 runs) | 185.3564 | 136.0209 |
| Average Time (ms / 10,000 runs) | 226.3868 | 141.3833 |
| Nodes Explored | 22 | 17 |

On this particular factory-floor layout, DFS had a lower average execution time
and explored fewer nodes than BFS. The result is specific to this input layout
and traversal order and does not mean DFS will always be faster.

## Verification

The generated results were checked by running the program multiple times. The same factory-floor input was used for both BFS and DFS to keep the comparison fair.

## AI Contribution Summary

AI was used mainly as a learning, planning, debugging, and documentation assistant. The actual program execution, profiling, timing measurements, result verification, and final experimental work were performed by me.