from crawler import Crawler

class MazeSolver:
	def __init__(self, maze, start_coords, end_coords):
		self.maze = maze
		self.start_x, self.start_y = start_coords
		self.end_x, self.end_y = end_coords
		self.num_of_squares = len(self.maze) * len(self.maze[0])

	def perform(self):
		finished = False
		counter = 0
		crawler = Crawler(self.start_x, self.start_y, self.maze)

		for i in range(self.num_of_squares):
			crawler_position = (crawler.x, crawler.y)
			# print(crawler_position)
			if crawler_position == (self.end_x, self.end_y):
				finished = True
				break
			crawler.perform()
			counter += 1

		return finished 