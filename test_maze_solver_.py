import unittest
from maze_solver import MazeSolver
from maze_parser import MazeParser

class MazeSolverTests(unittest.TestCase):

	# def setUp(self):


	def test_solves_valid_maze(self):
		parser = MazeParser('mazes/maze_pass.txt')
		self.maze, self.start_coords, self.end_coords = parser.perform()
		solver = MazeSolver(self.maze, self.start_coords, self.end_coords)
		self.assertTrue(solver.solve())

	def test_returns_from_unsolvable_maze(self):
		parser = MazeParser('mazes/maze_fail_no_solution.txt')
		self.maze, self.start_coords, self.end_coords = parser.perform()
		solver = MazeSolver(self.maze, self.start_coords, self.end_coords)
		self.assertFalse(solver.solve())
