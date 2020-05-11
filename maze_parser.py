class MazeParser:

	def __init__(self, maze_file):
		self.maze_file = maze_file

	def perform(self):
		with open(self.maze_file) as f:
			output = f.readlines()
			output = [line.strip() for line in output]
			print(output)


