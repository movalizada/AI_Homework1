# A* Search (Three Modes)

### Files
- `a_star.py` → Python implementation of A* search
- `input1.txt` → Small graph input
- `input2.txt` → Medium graph input

### Description
This program implements A* search in three modes:
1. **UCS (h=0)** – uniform cost search.
2. **A* Euclidean** – uses straight-line distance as heuristic.
3. **A* Manhattan** – uses Manhattan distance as heuristic.

### How to Run
```bash
python a_star.py
The program will read both input1.txt and input2.txt and print:

Optimal cost

Path found

Number of expanded nodes

Number of pushes

Maximum frontier size

Runtime

Notes
Input format: first lines define S,<start> and D,<goal>, followed by id,cell for nodes, and u,v,w for edges.

Supports reproducible runs for comparison.

###
=========== A* SMALL TEST ===========

UCS (h=0)
Path: 1 -> 2 -> 4 -> 6 -> 8
Total cost: 10
Expanded: 8
Runtime: 0.00000s

A* Euclidean
Path: 1 -> 2 -> 4 -> 6 -> 8
Total cost: 10
Expanded: 8
Runtime: 0.00000s

A* Manhattan
Path: 1 -> 2 -> 4 -> 6 -> 8
Total cost: 10
Expanded: 8
Runtime: 0.00000s

=========== A* MEDIUM TEST ===========

UCS (h=0)
Path: 1 -> 2 -> 6 -> 10
Total cost: 9
Expanded: 9
Runtime: 0.00000s

A* Euclidean
Path: 1 -> 2 -> 6 -> 10
Total cost: 9
Expanded: 7
Runtime: 0.00000s

A* Manhattan
Path: 1 -> 2 -> 6 -> 10
Total cost: 9
Expanded: 7
Runtime: 0.00000s
