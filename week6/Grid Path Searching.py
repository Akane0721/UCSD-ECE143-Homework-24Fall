from collections import deque


def count_paths(m, n, blocks):
    """
    Find the number of connected paths between the top-left square and the bottom right square by traversing only the intermediate squares with the . symbol

    Args:
        m (int): Height
        n (int): Width
        blocks (list): A list of tuples indicating the blocked # entries in the grid
    """
    assert isinstance(m, int) and isinstance(n, int) and isinstance(blocks, list)
    grid = [[0] * n for i in range(m)]
    for x, y in blocks:
        assert not (x == m - 1 and y == n - 1)
        grid[x][y] = 1
    cnt = 0
    vis = set()
    queue = deque()
    queue.append((0, 0))
    while len(queue):
        x, y = queue.popleft()
        if x == m - 1 and y == n - 1:
            cnt += 1
            continue
        if x + 1 < m and grid[x + 1][y] == 0:
            queue.append((x + 1, y))
        if y + 1 < n and grid[x][y + 1] == 0:
            queue.append((x, y + 1))
    return cnt


# print(count_paths(3, 4, [(0, 3), (1, 1)]))
