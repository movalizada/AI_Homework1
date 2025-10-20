def read_input(filename):
    colors = None
    edges = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("colors="):
                colors = int(line.split("=")[1])
            else:
                u, v = map(int, line.split(","))
                edges.append((u, v))
    return colors, edges


def build_graph(edges):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, set()).add(v)
        graph.setdefault(v, set()).add(u)
    return graph


def init_domains(graph, k):
    return {node: list(range(1, k + 1)) for node in graph}


def select_unassigned_var(domains, assignment):
    unassigned = [v for v in domains if v not in assignment]
    return min(unassigned, key=lambda v: len(domains[v]))


def order_values(var_name, domains, graph):
    neighbors = graph[var_name]
    def count_conflicts(value):
        return sum(value in domains[n] for n in neighbors)
    return sorted(domains[var_name], key=count_conflicts)


def revise(domains, x, y):
    revised = False
    for val in domains[x][:]:
        if all(v == val for v in domains[y]):
            domains[x].remove(val)
            revised = True
    return revised


def ac3(graph, domains):
    queue = [(x, y) for x in graph for y in graph[x]]
    while queue:
        x, y = queue.pop(0)
        if revise(domains, x, y):
            if not domains[x]:
                return False
            for z in graph[x]:
                if z != y:
                    queue.append((z, x))
    return True


def backtrack(assignment, graph, domains):
    if len(assignment) == len(graph):
        return assignment

    var = select_unassigned_var(domains, assignment)
    for value in order_values(var, domains, graph):
        if all(assignment.get(n) != value for n in graph[var]):
            local_domains = {v: list(domains[v]) for v in domains}
            assignment[var] = value
            if ac3(graph, local_domains):
                result = backtrack(assignment, graph, local_domains)
                if result:
                    return result
            del assignment[var]
    return None


def solve_csp(filename):
    colors, edges = read_input(filename)
    graph = build_graph(edges)
    domains = init_domains(graph, colors)
    result = backtrack({}, graph, domains)
    if result:
        print(f"SOLUTION for {filename}:", result)
    else:
        print(f"failure for {filename}")


if __name__ == "__main__":
    # Avtomatik olaraq iki faylı işlət
    solve_csp("csp_input1.txt")
    solve_csp("csp_input2.txt")
