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
    
    def test_maze_create_cells_more(self):
        cols = 500
        rows = 600
        maze = Maze(20, 20, rows, cols, 20, 20)
        self.assertEqual(len(maze._cells), cols)
        self.assertEqual(len(maze._cells[0]), rows)
        
    def test_maze_entrance_and_exit(self):
        cols = 10
        rows = 10
        size = 20
        maze = Maze(size, size, rows, cols, size, size)
        entrance = maze._cells[0][0]
        self.assertEqual(entrance.has_left_wall, False)
        exit = maze._cells[cols - 1][rows - 1]
        self.assertEqual(exit.has_right_wall, False)
        
if __name__ == "__main__":
    unittest.main()