from maze_solver import MazeSolver
from maze_parser import MazeParser

class MazeRunner:

	start_coords = (1, 10)
	end_coords = (78, 1)
	

	def __init__(self, maze_file):
		self.maze_file = maze_file

	def perform(self):
		parser = MazeParser(self.maze_file)
		self.maze = parser.perform()
		# import code; code.interact(local=dict(globals(), **locals()))
		print(self.maze)
		self.solver = MazeSolver(self.maze, self.start_coords, self.end_coords)
		return self.solver.solve()



runner = MazeRunner('mazes.txt')
runner.perform()
