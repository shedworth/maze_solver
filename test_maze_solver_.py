import unittest
from maze_solver import MazeSolver
from maze_parser import MazeParser

class MazeSolverTests(unittest.TestCase):

	def test_solves_valid_maze(self):
		parser = MazeParser('mazes/maze_pass.txt')
		parsed_maze = parser.perform()
		solver = MazeSolver(parsed_maze)
		self.assertTrue(solver.perform())

	def test_returns_from_unsolvable_maze(self):
		parser = MazeParser('mazes/maze_fail_no_solution.txt')
		parsed_maze = parser.perform()
		solver = MazeSolver(parsed_maze)
		self.assertFalse(solver.perform())
