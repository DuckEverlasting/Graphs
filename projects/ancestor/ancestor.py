
def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for i in ancestors:
        graph[i[1]] = []
    for i in ancestors:
        graph[i[1]] += [i[0]]

    queue = [[starting_node]]
    cleared = set()
    paths = []

    while len(queue):
        current = queue.pop(0)
        cleared.add(current[-1])
        for i in [current[-1]]:
            if i not in graph:
                if len(current) > 1:
                    paths.append(current)
            else:
                for j in graph[i]:
                    if j not in cleared:
                        queue.append(current + [j])

    if len(paths):
        max_path = paths[0]
        for i in paths:
            if len(i) > len(max_path):
                max_path = i
            if len(i) == len(max_path) and i[-1] < max_path[-1]:
                max_path = i
        return max_path[-1]
    else:
        return -1
