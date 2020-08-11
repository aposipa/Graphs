from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    tree = Graph()
    for (vert_1, vert_2) in ancestors:
        tree.add_vertex(vert_1)
        tree.add_vertex(vert_2)

    for (vert_1, vert_2) in ancestors:
        tree.add_edge(vert_1, vert_2)

    target_vert = None
    longest_path = 1

    for vert in tree.vertices:
        path = tree.dfs(vert, starting_node)

        if path:
            if len(path) > longest_path:
                longest_path = len(path)
                target_vert = vert
        elif not path and longest_path == 1:
            target_vert = -1

    return target_vert