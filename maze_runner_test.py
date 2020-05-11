import unittest
from maze_runner import MazeRunner

class MazeRunnerTests(unittest.TestCase):

	def test_solve_pass(self):
		maze_runner = MazeRunner('mazes.txt')
		self.assertTrue(maze_runner.perform())


	# def test_solve_fail(self):
	# 	maze_runner = MazeRunner()
