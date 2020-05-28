class Maze:
    """Maze object containing start and end coordinates (as
    (x, y) tuples), and a list of lists representing the maze itself"""
    def __init__(self, maze_map, start_coords, end_coords):
        self.maze_map = maze_map
        self.start_coords = start_coords
        self.end_coords = end_coords