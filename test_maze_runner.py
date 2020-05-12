import unittest
from maze_runner import MazeRunner

class MazeRunnerTests(unittest.TestCase):

	def test_solves_valid_maze(self):
		maze_runner = MazeRunner('mazes/maze_pass.txt')
		self.assertTrue(maze_runner.perform())

	def test_fails_invalid_maze(self):
		maze_runner = MazeRunner('mazes/maze_fail_no_solution.txt')
		self.assertFalse(maze_runner.perform())