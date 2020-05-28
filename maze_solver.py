from crawler import Crawler

class MazeSolver:
	"""Incrementally moves a Crawler object around the maze
	until either the end is reached, or the number of available
	elements in maze has been exhausted (maze is unsolvable)"""
	def __init__(self, parsed_maze):
		self.maze_map = parsed_maze.maze_map
		self.start_x, self.start_y = parsed_maze.start_coords
		self.end_x, self.end_y = parsed_maze.end_coords
		self.num_of_squares = len(self.maze_map) * len(self.maze_map[0])

	def perform(self):
		finished = False
		counter = 0
		crawler = Crawler(self.start_x, self.start_y, self.maze_map)

		for i in range(self.num_of_squares):
			crawler_position = (crawler.x, crawler.y)
			# print(crawler_position)
			if crawler_position == (self.end_x, self.end_y):
				finished = True
				break
			crawler.perform()
			counter += 1

		return finished 