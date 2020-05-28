import unittest
from crawler import Crawler
from base_objects import Maze

class CrawlerTests(unittest.TestCase):

	def setUp(self):
		maze_map = [
			"000000",
			"0  0 0 ",
			"0 00 0",
			"  0000"
		]
		start_x = 3
		start_y = 2

		self.crawler = Crawler(maze_map, start_x, start_y)
	
	# Test 'perform' method
	def test_turns_left_when_facing_wall(self):
		self.crawler.perform()
		self.assertEqual(self.crawler.x, 2)
		self.assertEqual(self.crawler.y, 2)
	
	"""Testing private methods"""	

	# Test '_movements_to_try' method
	def test_list_rotator_lambda(self):
		self.assertEqual(self.crawler._movements_to_try(), ["left", "up", "right", "down"])
		self.crawler.pointing = "left"
		self.assertEqual(self.crawler._movements_to_try(), ["down", "left", "up", "right"])
		self.crawler.pointing = "down"
		self.assertEqual(self.crawler._movements_to_try(), ["right", "down", "left", "up"])
		self.crawler.pointing = "right"
		self.assertEqual(self.crawler._movements_to_try(), ["up", "right", "down", "left"])


	# Test '_move_in_order' method
	def test_crawler_turns_180_degrees_when_facing_dead_end(self):
		self.crawler.x = 5
		self.crawler.y = 2
		self.crawler._move_in_order(["left", "up", "right", "down"])
		self.assertEqual(self.crawler.x, 5)
		self.assertEqual(self.crawler.y, 3)


	# Test '_shift' method
	def test_shift_left_moves_in_right_direction(self):
		self.crawler._shift("left")
		self.assertEqual(self.crawler.x, 2)
		self.assertEqual(self.crawler.y, 2)
		self.assertEqual(self.crawler.pointing, 'left')

	def test_shift_up_moves_in_right_direction(self):
		self.crawler._shift("up")
		self.assertEqual(self.crawler.x, 3)
		self.assertEqual(self.crawler.y, 1)
		self.assertEqual(self.crawler.pointing, 'up')

	def test_shift_right_moves_in_right_direction(self):
		self.crawler._shift("right")
		self.assertEqual(self.crawler.x, 4)
		self.assertEqual(self.crawler.y, 2)
		self.assertEqual(self.crawler.pointing, 'right')

	def test_shift_down_moves_in_right_direction(self):
		self.crawler._shift("down")
		self.assertEqual(self.crawler.x, 3)
		self.assertEqual(self.crawler.y, 3)
		self.assertEqual(self.crawler.pointing, 'down')


	# Test '_is_space' method
	def test_is_space_detects_space(self):
		self.assertTrue(self.crawler._is_space("left"))

	def test_is_space_detects_wall(self):
		self.assertFalse(self.crawler._is_space("right"))

	def test_is_space_detects_edge_of_maze(self):
		self.crawler.x = 1
		self.crawler.y = 4
		self.assertFalse(self.crawler._is_space("left"))
