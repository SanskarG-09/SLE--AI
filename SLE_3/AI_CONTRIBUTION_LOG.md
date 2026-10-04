# AI Contribution Log: SLE-3 (Architectural Design, Full C4 Model)

**Course:** 02AML204 – Introduction to Artificial Intelligence
**Name:** Sanskar Gorave | **PRN:** 25UAM126 | **Division:** B
**Date:** 04/10/2026
**AI tools used:** ChatGPT and Claude

This log records which parts of SLE-3 were done with AI help and which parts I did myself.

---

## 1. Summary

| Part of the work | AI helped? | Who did what |
|---|---|---|
| Choosing the system | No | I chose my SLE-2 BFS vs DFS factory-floor system as the base for SLE-3. |
| `factory_search.py` (BFS, DFS, timing) | Yes | The code was taken from AI. I ran it in VS Code. |
| Reading the SLE-3 guideline | Yes | ChatGPT and Claude read the guideline and explained it step by step. |
| C4 structure (what goes at each level) | Yes | AI suggested the structure. I gave the instructions one step at a time. |
| Diagrams (Context, Container, Component) | Yes | Claude created them as editable draw.io files. I opened them in draw.io and exported the PNG images. |
| Text of the report sections | Yes | AI drafted the wording. I approved each section step by step. |
| Word report file | Yes | Claude built the `.docx` from the approved sections and my exported diagrams. |

---

## 2. Step-by-step log

### ChatGPT
- Read the SLE-3 guideline file and summarised what it asks for.
- Matched the report structure to the guideline's template.
- Confirmed it would work one step at a time, only on my instruction.
- Asked for the report date, and I gave it.

### Claude
- Read the SLE-3 guideline and `factory_search.py`, and described what the code contains and what it does not (no classes, no A*, no path output).
- Drafted the text for Sections 1 to 8 one step at a time, using the real names from my code.
- Created the Context, Container and Component diagrams as `.drawio` files.
- Re-ran the search code to confirm the node counts quoted in the report (BFS 22, DFS 17).
- Built the Word report and checked that it fits in 2 pages.

### Me
- Chose the system and decided to continue from SLE-2.
- Ran `factory_search.py` in VS Code.
- Opened the `.drawio` files in draw.io and exported them as PNG images.
- Directed the work one section at a time and approved or rejected each step.

---

## 3. Changes I asked for after reviewing AI output

- **Section 5 (Code Level):** I said it did not match, and it was rewritten to list only real functions and the grid.
- **Diagram format:** I asked for the diagrams in draw.io instead of images drawn by code.
- **Diagram labels:** a label overlapped a box in the Component diagram, and it was fixed.

---

## 4. What was and was not checked

- **Checked:** the BFS and DFS node counts (22 and 17) were confirmed by running the code.
- **Not re-run:** the timing figures (BFS 226.39 ms, DFS 141.38 ms per 10,000 searches) come from my SLE-2 report. They depend on the machine.
- **Honest limits:** the code, the structure and the wording came from AI. My own work was choosing the system, running the code, exporting the diagrams and approving the content.
