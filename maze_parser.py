from base_objects import Maze

class MazeParser:
	"""Takes a .txt file and returns a Maze object if it contains
	a valid maze. A valid maze is a .txt file containing a S
	(representing the starting point) and a F (representing
	the ending point"""
	def __init__(self, maze_file):
		self.maze_file = maze_file

	def perform(self):
		start_coords = None
		end_coords = None
		with open(self.maze_file) as f:
			output = f.readlines()
			output = [line.strip('\n') for line in output]
			for y in range(len(output)):
				for x in range(len(output[y])):
					if output[y][x] == "S":
						start_coords = (x+1, y+1)
					if output[y][x] == "F":
						end_coords = (x+1, y+1) 
				if start_coords and end_coords:
					return Maze(output, start_coords, end_coords)

