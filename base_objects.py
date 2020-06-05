from collections import namedtuple

Maze = namedtuple("Maze", ["maze_map", "start_coords", "end_coords"])
CrawlerPosition = namedtuple("CrawlerPosition", ["x", "y", "direction"])