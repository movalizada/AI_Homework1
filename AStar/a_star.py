import math
import time

# --- Read graph from file ---
def read_graph(filename):
    vertices = {}
    edges = {}
    start = None
    goal = None

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith("S,"):
                start = int(line.split(",")[1])
            elif line.startswith("D,"):
                goal = int(line.split(",")[1])
            else:
                parts = list(map(int, line.split(",")))
                if len(parts) == 2:
                    v, cell = parts
                    vertices[v] = cell
                    edges.setdefault(v, [])
                elif len(parts) == 3:
                    u, v, w = parts
                    edges.setdefault(u, []).append((v, w))
                    edges.setdefault(v, []).append((u, w))

    return vertices, edges, start, goal


# --- Coordinate computation for heuristic ---
def compute_coords(vertices):
    coords = {}
    for vid, cell in vertices.items():
        x = cell // 10
        y = cell % 10
        coords[vid] = (x, y)
    return coords


# --- Heuristic functions ---
def h_zero(a, b, coords):
    return 0

def h_euclidean(a, b, coords):
    x1, y1 = coords[a]
    x2, y2 = coords[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def h_manhattan(a, b, coords):
    x1, y1 = coords[a]
    x2, y2 = coords[b]
    return abs(x1 - x2) + abs(y1 - y2)


# --- A* algorithm ---
def a_star(graph, coords, start, goal, heuristic):
    g = {start: 0}
    parent = {start: None}
    frontier = [(0, start)]

    expanded = 0
    t0 = time.time()

    while frontier:
        frontier.sort(key=lambda x: x[0])
        f_val, node = frontier.pop(0)
        expanded += 1

        if node == goal:
            t1 = time.time()
            return build_result(True, parent, goal, g[goal], expanded, t1 - t0)

        for neigh, w in graph.get(node, []):
            new_g = g[node] + w
            if new_g < g.get(neigh, float("inf")):
                g[neigh] = new_g
                parent[neigh] = node
                f_score = new_g + heuristic(neigh, goal, coords)
                frontier.append((f_score, neigh))

    t1 = time.time()
    return build_result(False, parent, goal, None, expanded, t1 - t0)


# --- Build result ---
def build_result(found, parent, goal, cost, expanded, runtime):
    if not found:
        return {"found": False, "cost": None, "path": None, "expanded": expanded, "runtime": runtime}

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return {"found": True, "cost": cost, "path": path, "expanded": expanded, "runtime": runtime}


# --- Print results ---
def show_result(res, mode):
    print(f"\n{mode}")
    if res["found"]:
        print(f"Path: {' -> '.join(map(str, res['path']))}")
        print(f"Total cost: {res['cost']}")
    else:
        print("No path found")
    print(f"Expanded: {res['expanded']}")
    print(f"Runtime: {res['runtime']:.5f}s")


# --- Run tests ---
def run(filename):
    vertices, edges, start, goal = read_graph(filename)
    coords = compute_coords(vertices)

    tests = [
        (h_zero, "UCS (h=0)"),
        (h_euclidean, "A* Euclidean"),
        (h_manhattan, "A* Manhattan")
    ]

    for h_func, name in tests:
        result = a_star(edges, coords, start, goal, h_func)
        show_result(result, name)


if __name__ == "__main__":
    print("=========== A* SMALL TEST ===========")
    run("AStar/astar_input1.txt")
    print("\n=========== A* MEDIUM TEST ===========")
    run("AStar/astar_input2.txt")