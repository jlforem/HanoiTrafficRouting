import heapq
from typing import List, Tuple

def find_fastest_route(grid: List[List[int]]) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Find the fastest route through the Hanoi traffic grid from top-left to bottom-right.
    Roads have a time cost; some may be blocked (-1). Allowed movement: up, down, left, right.
    
    Returns:
        total_time (int): total travel time
        path (List[Tuple[int, int]]): coordinates from start to end
    """
    # TODO: Implement Dijkstra's or A* algorithm
    
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if grid[0][0] == -1 or grid[rows-1][cols-1] == -1:
        return float('inf'), []

    heap = [(grid[0][0], 0, 0, [(0, 0)])]  # (cost, x, y, path)
    visited = set()

    while heap:
        cost, x, y, path = heapq.heappop(heap)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == (rows - 1, cols - 1):
            return cost, path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] != -1 and (nx, ny) not in visited:
                    new_cost = cost + grid[nx][ny]
                    new_path = path + [(nx, ny)]
                    heapq.heappush(heap, (new_cost, nx, ny, new_path))

    return float('inf'), []