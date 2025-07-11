import heapq  # We use this to always pick the fastest option so far

def find_fastest_route(traffic_grid):
    number_of_rows = len(traffic_grid)
    number_of_columns = len(traffic_grid[0])

    # ✅ 1. If start or end is blocked, return no route
    if traffic_grid[0][0] == -1 or traffic_grid[number_of_rows - 1][number_of_columns - 1] == -1:
        return (float('inf'), [])

    # ✅ 2. Setup tracking grid and starting point
    shortest_time_grid = [[float('inf')] * number_of_columns for _ in range(number_of_rows)]
    shortest_time_grid[0][0] = traffic_grid[0][0]

    # ✅ 3. Priority queue for exploring fastest options first
    priority_queue = [(traffic_grid[0][0], 0, 0, [(0, 0)])]  # (time_so_far, row, col, path_so_far)

    # ✅ 4. Valid movement directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while priority_queue:
        # ✅ Get the next best option
        current_time, current_row, current_col, path_so_far = heapq.heappop(priority_queue)

        # ✅ Check if we've reached the bottom-right destination
        if (current_row, current_col) == (number_of_rows - 1, number_of_columns - 1):
            return (current_time, path_so_far)

        # 🔄 Try moving in all four directions
        for dr, dc in directions:
            next_row = current_row + dr
            next_col = current_col + dc

            # ✅ Skip if out of bounds
            if not (0 <= next_row < number_of_rows and 0 <= next_col < number_of_columns):
                continue

            # ✅ Skip blocked cells
            if traffic_grid[next_row][next_col] == -1:
                continue

            # ✅ Calculate time to reach next cell
            new_time = current_time + traffic_grid[next_row][next_col]

            # ✅ Only continue if this is a faster path
            if new_time < shortest_time_grid[next_row][next_col]:
                shortest_time_grid[next_row][next_col] = new_time
                new_path = path_so_far + [(next_row, next_col)]
                heapq.heappush(priority_queue, (new_time, next_row, next_col, new_path))

    # ❌ If we finish and never reached the goal
    return (float('inf'), [])
