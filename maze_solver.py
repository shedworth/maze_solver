from crawler import Crawler
from base_objects import CrawlerPosition


"""Define a segment"""
class Segment:
	def __init__(self, coords, parent=None):
		self.coords = [coords]
		self.direction = None
		self.children = []
		self.parent = parent

	def __repr__(self):
		return str([child.coords for child in self.children])

"""Manager class"""
class MazeSolver:
	def __init__(self, parsed_maze):
		self.maze_map = parsed_maze.maze_map
		self.start_x, self.start_y = parsed_maze.start_coords
		self.end_x, self.end_y = parsed_maze.end_coords
		self.current_position = CrawlerPosition(self.start_x, self.start_y, "left")
		#Blacklist of visited coords not to revisit
		self.visited_coords = set()
		self.visited_coords.add((self.start_x, self.start_y))
		self.state = FirstSegment()
		#Root segment containing all others as children
		self.root = Segment((self.start_x, self.start_y))
		self.current_segment = None

	def perform(self):
		finished = False
		for i in range(self._num_of_squares()):
		# for i in range(300):
			# print("\n")
			# print(f"Root: {self.root}")
			# print(f"Visited_coords: {self.visited_coords}")
			# Move crawler
			crawler = Crawler(self.maze_map, self.current_position.x, self.current_position.y, self.current_position.direction)
			# print(f"Current direction: {self.current_position.direction}")
			new_position = crawler.perform()
			# print(f"New x/y: ({new_position.x},{new_position.y}), New pos: {new_position.direction}")
			# If space has been visited already, nudge crawler right and try again
			while (new_position.x, new_position.y) in self.visited_coords and self._has_turned_90(self.current_position.direction, new_position.direction):
				#Move crawler back
				crawler.x, crawler.y = self.current_position.x, self.current_position.y
				#Nudge crawler to right
				# print(f"Prenudge: {crawler.x}, {crawler.y}, {crawler.pointing}")
				crawler.flip()
				# print(f"Postnudge: {crawler.x}, {crawler.y}, {crawler.pointing}")
				# print("nudge crawler")
				#Try again
				new_position = crawler.perform()
				# print(f"Postnudge new pos x/y: ({new_position.x},{new_position.y}), Postnudge: {new_position.direction}")

			if new_position.x == self.end_x and new_position.y == self.end_y:
				# print("finish condition met")
				finished = True
				break
			self.visited_coords.add((new_position.x, new_position.y))
			#Skip this line on first move
			if not isinstance(self.state, FirstSegment):
				self._choose_state(new_position)
				# print(f"{self.state} chosen")
			"""All states just return new_position, except EndSegment, which sets current
			position to end of last segment"""
			self.current_position = self.state.process(new_position, self)
			# Recursively call function again
			return self.perform()

		"""Return list of output coords"""		
		if finished:
			# print("Finished")
			segments = [self.root]
			output_coords = []
			while segments:
				segment = segments.pop(0)
				output_coords.extend(segment.coords)
				segments = segment.children + segments

			return output_coords
		else:
			return []

	def _choose_state(self, crawler_position):
		if crawler_position.direction == self.current_position.direction:
			self.state = Continue()
		elif self._has_turned_90(self.current_position.direction, crawler_position.direction):
			self.state = StartSegment()
		elif self._has_turned_180(self.current_position.direction, crawler_position.direction):
			self.state = EndSegment()


	def _has_turned_90(self, old_direction, new_direction):
		if (old_direction == "up") and (new_direction == "left" or new_direction == "right"):
			return True
		if (old_direction == "left") and (new_direction == "up" or new_direction == "down"):
			return True
		if (old_direction == "down") and (new_direction == "left" or new_direction == "right"):
			return True
		if (old_direction == "right") and (new_direction == "up" or new_direction == "down"):
			return True

	def _has_turned_180(self, old_direction, new_direction):
		if old_direction == "up" and new_direction == "down": 
			return True
		if old_direction == "left" and new_direction == "right":
			return True
		if old_direction == "down" and new_direction == "up":
			return True
		if old_direction == "right" and new_direction == "left":
			return True

	def _num_of_squares(self):
		return len(self.maze_map) * len(self.maze_map[0])


"""Define some states"""
class FirstSegment:
	"""Creates first segment and sets root of MazeSolver"""
	def process(self, crawler_position, solver):
		# print("processing first segment")
		"""Create new segment with solver.root as parent"""
		segment = Segment((crawler_position.x, crawler_position.y), parent=solver.root)
		solver.current_segment = segment
		"""Add segment to children of solver.root"""
		solver.root.children.append(solver.current_segment)
		"""Remove FirstSegment state to invoke solver's state chooser"""
		solver.state = None
		return crawler_position


class StartSegment:
	"""Creates new segment, sets as current segment and appends 
	to children of previous segment"""
	def process(self, crawler_position, solver):
		# print("processing StartSegment")
		#Set direction indicator on current segment before beginning new segment
		last_coord_of_current_segment = solver.current_segment.coords.pop()
		# print(f"removing {last_coord_of_current_segment}")
		solver.visited_coords.remove(last_coord_of_current_segment)
		solver.current_segment.direction = solver.current_position.direction
		#Create new segment with current_segment as parent
		segment = Segment((last_coord_of_current_segment), parent=solver.current_segment)
		segment.coords.append((crawler_position.x, crawler_position.y))
		#Add new segment to children of current_segment
		solver.current_segment.children.append(segment)
		#Set surrent segment to new segment
		solver.current_segment = segment
		return crawler_position


class Continue:
	"""Adds co-ordinate to current segment's list of
	co-ordinates"""
	def process(self, crawler_position, solver):
		# print("processing Continue")
		solver.current_segment.coords.append((crawler_position.x, crawler_position.y))
		return crawler_position


class EndSegment:
	"""A dead end has been reached. Remove segment from previous 
	segment's children"""
	def process(self, crawler_position, solver):
		# print("processing EndSegment")
		"""Set current_segment to parent of current_segment"""
		solver.current_segment = solver.current_segment.parent
		"""Discard dead segment"""
		solver.current_segment.children.pop()
		"""Return position of end of last segment"""
		return CrawlerPosition(
			solver.current_segment.coords[-1][0],
			solver.current_segment.coords[-1][1],
			solver.current_segment.direction
		)



