# AI Contribution Log – SLE-4

**Course:** 02AML204 – Introduction to Artificial Intelligence
**Name:** Sanskar Gorave | **PRN:** 25UAM126 | **Division:** B
**Date:** 10/10/2026
**GitHub:** https://github.com/SanskarG-09/SLE--AI.git

## 1. Project Description

SLE-4 is the Final Viva & Architecture Decision Record (ADR) for my Factory-Floor Search System. The ADR records one design decision: **Use of a Visited Set and Algorithm-Specific Frontier Data Structures in BFS and DFS**.

- BFS uses a FIFO queue (`collections.deque`).
- DFS uses a LIFO stack (a Python list).
- Both use a visited set of (row, col) cells on the same 6×6 grid.

The decision is justified using my SLE-2 profiling results and my SLE-3 C4 architecture.

## 2. Tools and Technologies

| Tool | Used for |
|---|---|
| Python (`factory_search.py`) | BFS and DFS on the factory grid, node counts and timing |
| Microsoft Word | Final SLE-4 document (`SLE4_25UAM126_SanskarGorave.docx`) |
| Claude (AI) | Drafting and checking the SLE-4 document, README and this log |
| Earlier SLEs | VS Code, `py-spy`, `perf_counter()`, draw.io, Git/GitHub, ChatGPT (SLE-2), ChatGPT and Claude (SLE-3) |

## 3. AI Contributions (SLE-4)

| Task | What AI did |
|---|---|
| Reading the files | Read my SLE-1 README, SLE-2 report, SLE-3 report, the SLE-4 guideline and `factory_search.py` |
| Structure | Organised the document in the faculty structure: cover details, ADR, journey summary, AI note |
| ADR writing | Drafted the Context, Decision, Alternatives, Rationale, Consequences and References from my reports and code |
| Checking the facts | Ran the code to confirm 22 BFS nodes and 17 DFS nodes, and checked the timings, name, PRN, division and dates against my reports |
| Observations from the code | Pointed out that the code marks a cell visited when it is discovered, that DFS tries the right-hand neighbour first, and that the code returns only the node count, not the path |
| File creation | Generated the Word file, then shortened and simplified it after my review |
| Supporting files | Drafted this contribution log and the SLE-4 README |

## 4. My Personal Contributions

**From the conversation:**
- I proposed the ADR decision and its title, and told the AI which results and architecture points to use.
- I supplied my own SLE-1, SLE-2 and SLE-3 files and the Python code, and told the AI not to invent features, results or contributions.
- I reviewed the first draft and asked for a simpler, less repetitive version, keeping the ADR decision and SLE-2 numbers, with Part D removed.

**From my earlier reports (SLE-2 and SLE-3):**
- I created and ran the BFS vs DFS experiment in VS Code, generated the `py-spy` flame graphs, and collected the performance numbers.
- I chose the SLE-2 system as the base for SLE-3, ran `factory_search.py`, and exported the C4 diagrams from draw.io.

**[EDIT]** Add anything else you did yourself for SLE-4, for example checking the ADR against your own code, changing the wording, or practising for the viva. Delete this line if there is nothing to add.

## 5. Review and Changes

- The first draft was 3 pages and included viva preparation notes. I asked for a shorter, simpler version and for Part D to be removed. The final document is 2 pages.
- The SLE-2 numbers (average 226.3868 ms for BFS and 141.3833 ms for DFS per 10,000 searches; 22 and 17 nodes) and the ADR decision were kept.
- The ADR does not say DFS is always better. It says DFS was faster on this grid and traversal order, and that BFS keeps the shortest-path guarantee.

## 6. Learning Outcomes

**[EDIT]** Keep only the points you can explain in the viva:

- What an ADR is and how to record one decision with context, alternatives, rationale and consequences
- Why BFS uses a queue and DFS uses a stack
- Why a visited set stops repeated exploration
- How to separate measured results (SLE-2) from theory (BFS shortest path)
- How the decision connects to the SLE-3 architecture

## 7. Possible Future Improvements

- Return the actual path found, so path length can be compared
- Test larger and different grids before drawing conclusions
- Try A* with a heuristic, as suggested in my SLE-3 conclusion

## 8. Honesty Statement

AI was used to help draft and check the SLE-4 document. The decision, the evidence (SLE-2 and SLE-3) and the code come from my own project, and I will explain and defend them in the viva.
