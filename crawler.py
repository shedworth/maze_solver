class Crawler:
	"""Moves to the next available space on a maze map, starting at the
	specified start co-ordinates and returns its new position"""	
	def __init__(self, maze_map, start_x, start_y):
		# import code; code.interact(local=dict(globals(), **locals()))

		self.x, self.y = start_x, start_y
		self.maze_map = maze_map
		self.pointing = "up"

	"""Coefficients for use in other methods:
	[list rotation index, x _shift, y _shift, symbol]"""
	directions = {
		"up": [0, 0, -1, "^"],		
		"right": [1, 1, 0, ">"],	
		"down": [2, 0, 1, "v"],
		"left": [3, -1, 0, "<"]
		}

	def perform(self):						
		# Crawl one space starting from leftmost available path
		movement_list = self._movements_to_try()
		self._move_in_order(movement_list)

	"""Private Methods"""

	def _movements_to_try(self):
		cls = self.__class__
		movements = ["left", "up", "right", "down"]
		movement_idx = cls.directions[self.pointing][0]
		list_rotator = lambda lst, n: lst[n:] + lst[:n]
		movements = list_rotator(movements, movement_idx)
		return movements

	def _move_in_order(self, direction_list): 
		# Attempts to move crawler in order of preference
		for direction in direction_list:
			if self._is_space(direction):
				self._shift(direction)
				break

	def _shift(self, direction):
		# Move crawler into adjacent empty space and updates direction pointer
		cls = self.__class__
		self.x = self.x+cls.directions[direction][1]
		self.y = self.y+cls.directions[direction][2]
		self.pointing = direction
		# print(cls.directions[direction][3])		# Print direction indicator (<>^v)

	def _is_space(self, direction):				
		# Check if adjacent space is a path or wall
		cls = self.__class__
		row = self.x+cls.directions[direction][1] - 1
		column = self.y+cls.directions[direction][2] - 1
		try:
			if self.maze_map[column][row] == " " or self.maze_map[column][row] == "F": 
			# Is a path
				return True
			else:
			# Is a wall
				return False
		except IndexError:
		# Is edge of maze_map (first/last index in row or column array)
			return False