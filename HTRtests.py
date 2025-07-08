import unittest
from hanoiTrafficRouting import find_fastest_route

class TestHanoiTraffic(unittest.TestCase):

    def test_basic_clear_grid(self):
        print("Test 1: Smooth ride from West Lake to Old Quarter...")
        grid = [
            [1, 3, 1, 5],
            [4, 1, 1, 1],
            [4, 3, 2, 1],
            [5, 1, 1, 1]
        ]
        time, path = find_fastest_route(grid)
        print(f"Travel time: {time} mins | Route: {path}")
        self.assertEqual(time, 7, "Should take 7 minutes on optimal path")
        self.assertTrue(path[0] == (0, 0) and path[-1] == (3, 3))

    def test_with_traffic_jam(self):
        print("Test 2: Jam near Kim Ma — rerouting...")
        grid = [
            [1, 3, -1, 5],
            [4, -1, 1, 1],
            [4, 3, 2, 1],
            [5, 1, 1, 1]
        ]
        time, path = find_fastest_route(grid)
        print(f"Jammed! Took {time} mins | Route: {path}")
        self.assertTrue(time > 7, "Jam should increase travel time")

    def test_fully_blocked(self):
        print("Test 3: Flooding at Cầu Giấy — no way through...")
        grid = [
            [1, -1],
            [-1, 1]
        ]
        result = find_fastest_route(grid)
        print("No route available.")
        self.assertEqual(result, (float('inf'), []), "No path should return infinity time and empty path")

    def test_already_at_destination(self):
        print("Test 4: Already at home in Hồ Tây. No travel needed.")
        grid = [[0]]
        time, path = find_fastest_route(grid)
        print(f"Instant arrival: {time} mins | Route: {path}")
        self.assertEqual(time, 0)
        self.assertEqual(path, [(0, 0)])

if __name__ == '__main__':
    print("Testing realistic Hanoi traffic... please wait for green light...")
    unittest.main()