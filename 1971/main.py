def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    del n

    seen = {source: True}
    queue = [
        source,
    ]

    neighbours: dict[int, list[int]] = {}
    for edge in edges:
        e0 = neighbours.get(edge[0], [])
        e0.append(edge[1])
        neighbours[edge[0]] = e0

        e1 = neighbours.get(edge[1], [])
        e1.append(edge[0])
        neighbours[edge[1]] = e1

    while len(queue) > 0:
        root = queue.pop(0)

        for edge in neighbours.get(root, []):
            if not seen.get(edge, False):
                queue.append(edge)
                seen[edge] = True

    return seen.get(destination, False)


if __name__ == "__main__":
    assert valid_path(
        n=3,
        edges=[[0, 1], [1, 2], [2, 0]],
        source=0,
        destination=2,
    )
