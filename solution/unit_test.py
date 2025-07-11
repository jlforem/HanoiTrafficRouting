import unittest
from main import find_fastest_route

# Check if route is using only adjacent cells
def fCheckRoute(Path):
    
    prevCell = (0,0)
    
    # Iteriate through the route
    for cell in Path:
        deltaCell = prevCell[0] - cell[0], prevCell[1] - cell[1]
        deltaCell = abs(deltaCell[0]), abs(deltaCell[1])
        
        if(deltaCell[0] + deltaCell[1] > 1):
            return False
        
        prevCell = cell
        
    return True

class TestHanoiTraffic(unittest.TestCase):

    def test_00_basic_clear_grid(self):
        print()
        print("---------------------------------------------------")
        print()
        print("Test 1: Smooth ride from West Lake to Old Quarter...")
        grid = [
            [1, 3, 1, 5],
            [4, 1, 1, 1],
            [4, 3, 2, 1],
            [5, 1, 1, 1]
        ]
        time, path = find_fastest_route(grid)
        self.assertTrue(fCheckRoute(path), "Route is not valid")
        print(f"Travel time: {time} mins | Route: {path}")
        self.assertEqual(time, 9, "Should take 9 minutes on optimal path")
        print("Should take 9 minutes on optimal path")
        self.assertTrue(path[0] == (0, 0) and path[-1] == (3, 3))
    def test_01_with_traffic_jam_no_rerouting(self):
        print()
        print("---------------------------------------------------")
        print()
        print("Test 2: Jam at Kim Ma — control test without rerouting...")
        grid = [
            [1, 3, 1, 5],
            [4, 1, 1, 1],
            [4, 3, 2, 1],
            [5, 1, 1, 1]
        ]
        time, path = find_fastest_route(grid)
        self.assertTrue(fCheckRoute(path), "Route is not valid")
        print(f"Travel time: {time} mins | Route: {path}")
        self.assertEqual(time, 9, "Should take 9 minutes on optimal path despite jam")
        print("Should take 9 minutes on optimal path despite jam")
        
    def test_02_with_traffic_jam(self):
        print()
        print("Continued: Jam near Kim Ma — Same grid, now with the traffic, now rerouting...")
        grid = [
            [1, 3, -1, 5],
            [4, -1, 1, 1],
            [4, 3, 2, 1],
            [5, 1, 1, 1]
        ]
        time, path = find_fastest_route(grid)
        self.assertTrue(fCheckRoute(path), "Route is not valid")
        print(f"Jammed! Took {time} mins | Route: {path}")
        print("Should reroute around the jam, increasing travel time.")
        self.assertTrue(time > 9, "Jam should increase travel time")

    def test_03_fully_blocked(self):
        print()
        print("---------------------------------------------------")
        print()
        print("Test 3: Flooding at Cầu Giấy — no way through...")
        grid = [
            [1, -1],
            [-1, 1]
        ]
        result = find_fastest_route(grid)
        self.assertTrue(fCheckRoute(result[1]), "Route is not valid")
        print(f"Flooded! Result: {result}")
        print("No route available.")
        self.assertEqual(result, (float('inf'), []), "No path should return infinity time and empty path")

    def test_04_already_at_destination(self):
        print()
        print("---------------------------------------------------")
        print()
        print("Test 4: Already at home in Hồ Tây. No travel needed.")
        grid = [[0]]
        time, path = find_fastest_route(grid)
        self.assertTrue(fCheckRoute(path), "Route is not valid")
        print(f"Instant arrival: {time} mins | Route: {path}")
        print("Should return zero time and path with single cell.")
        self.assertEqual(time, 0)
        self.assertEqual(path, [(0, 0)])
    
    def test_05_large_grid_with_multiple_routes(self):
        print()
        print("---------------------------------------------------")
        print()
        print("Test 5: Navigating through Hanoi's busy streets...")
        grid = [
            [1, 2, 3, 4, 5, 4],
            [2, -1, 1, -1, 1, 2],
            [3, 1, 2, 1, 2, -1],
            [4, -1, -1, 1, 3, -1],
            [5, 2, 1, 2, 1, -1],
            [1, 1, 1, 1, 1, 4]
        ]
        time, path = find_fastest_route(grid)
        print(f"Complex route: {time} mins | Route: {path}")
        print("Should return a valid route with reasonable time.")
        self.assertTrue(fCheckRoute(path), "Route is not valid")
        self.assertTrue(time < float('inf'), "Should find a valid route")
        self.assertTrue(path[0] == (0, 0) and path[-1] == (5, 5))

if __name__ == '__main__':
    print("Testing realistic Hanoi traffic... please wait for green light...")
    unittest.main()