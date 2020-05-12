from maze_solver import MazeSolver
from maze_parser import MazeParser

class MazeRunner:	

	def __init__(self, maze_file):
		self.maze_file = maze_file

	def perform(self):
		parser = MazeParser(self.maze_file)
		(self.maze, self.start_coords, self.end_coords) = parser.perform()
		solver = MazeSolver(self.maze, self.start_coords, self.end_coords)
		return solver.perform()
		

		# import code; code.interact(local=dict(globals(), **locals()))