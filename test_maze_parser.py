import unittest
from maze_parser import MazeParser

class MazeParserTests(unittest.TestCase):

	def test_parses_valid_maze(self):
		parser = MazeParser('mazes/maze_pass.txt')
		parsed_maze = parser.perform()
		self.assertEqual(parsed_maze.start_coords, (1, 10))
		self.assertEqual(parsed_maze.end_coords, (78, 1))

	def test_doesnt_parse_maze_with_missing_start_point(self):
		parser = MazeParser('mazes/maze_fail_no_start_marker.txt')
		self.assertFalse(parser.perform())

	def test_doesnt_parse_maze_with_missing_end_point(self):
		parser = MazeParser('mazes/maze_fail_no_finish_marker.txt')
		self.assertFalse(parser.perform())