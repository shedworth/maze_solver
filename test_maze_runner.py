import unittest
from maze_runner import MazeRunner

class MazeRunnerTests(unittest.TestCase):

	def test_solves_valid_maze(self):
		maze_runner = MazeRunner('mazes/maze_pass.txt')
		self.assertTrue(maze_runner.perform())

	def test_solves_valid_irregular_shaped_maze(self):
		maze_runner = MazeRunner('mazes/maze_pass_triangular_maze.txt')
		self.assertTrue(maze_runner.perform())		

	def test_solves_valid_maze_with_empty_space(self):
		maze_runner = MazeRunner('mazes/maze_pass_empty_space_maze.txt')
		self.assertTrue(maze_runner.perform())				

	def test_solves_maze_with_open_side(self):
		maze_runner = MazeRunner('mazes/maze_pass_with_open_side.txt')
		self.assertTrue(maze_runner.perform())

	def test_fails_maze_with_blockage(self):
		maze_runner = MazeRunner('mazes/maze_fail_no_solution.txt')
		self.assertFalse(maze_runner.perform())

