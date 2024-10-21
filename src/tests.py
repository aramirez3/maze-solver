import unittest

from window import *

from maze import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_entrance_and_exit(self):
        cols = 10
        rows = 10
        size = 20
        maze = Maze(0, 0, rows, cols, size, size)
        self.assertEqual(maze._cells[0][0].has_left_wall, False)
        self.assertEqual(maze._cells[cols - 1][rows - 1].has_right_wall, False)
        
if __name__ == "__main__":
    unittest.main()