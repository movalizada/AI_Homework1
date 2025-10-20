# CSP Graph Coloring

### Files
- `csp.py` → Python implementation of CSP graph coloring
- `input1.txt` → Small test graph (4 nodes, 3 colors)
- `input2.txt` → Medium test graph (6 nodes, 4 colors)

### Description
Solves the graph coloring problem using:
- **Backtracking search**
- **MRV (Minimum Remaining Values)**
- **LCV (Least Constraining Value)**
- **AC-3 (Arc Consistency)**

### How to Run
```bash
python csp.py input1.txt
python csp.py input2.txt
The program prints either:

css
Kodu kopyala
SOLUTION: {node: color, ...}
or

nginx
Kodu kopyala
failure
Notes
Each node is represented by an integer.

Colors are integers from 1 to colors specified in the input file.

Input format: colors=<k> followed by edges u,v.
