import unittest
from maze_runner import MazeRunner

class MazeRunnerTests(unittest.TestCase):

	def test_solve(self):
		maze_runner = MazeRunner()
		self.assertTrue(maze_runner.perform())