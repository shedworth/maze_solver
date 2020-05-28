from crawler import Crawler

class MazeSolver:
	"""Incrementally moves a Crawler object around the maze
	until either the end is reached, or the number of available
	elements in maze has been exhausted (maze is unsolvable)"""
	def __init__(self, parsed_maze):
		self.maze_map = parsed_maze.maze_map
		self.start_x, self.start_y = parsed_maze.start_coords
		self.end_x, self.end_y = parsed_maze.end_coords
	
	def perform(self):
		finished = False
		counter = 0
		crawler = Crawler(self.maze_map, self.start_x, self.start_y)

		"""For loop prevents crawler from endlessly moving
		around an unsolvable maze by returning after all squares
		have been visited"""
		for i in range(self._num_of_squares()):
			crawler_position = (crawler.x, crawler.y)
			if crawler_position == (self.end_x, self.end_y):
				finished = True
				break
			#Move crawler one space
			crawler.perform()
			counter += 1

		return finished 

	"""Private Methods"""

	def _num_of_squares(self):
		return len(self.maze_map) * len(self.maze_map[0])