from maze_solver import MazeSolver
from maze_parser import MazeParser

class MazeManager:	
    """Manager object that accepts maze as txt file and calls subordinate
    objects to parse maze to a nested list and then solve it."""
    def __init__(self, maze_file):
        self.maze_file = maze_file

    def perform(self):
        parser = MazeParser(self.maze_file)
        #Parser returns Maze object
        parsed_maze = parser.perform()
        solver = MazeSolver(parsed_maze)
        return solver.perform()


# import code; code.interact(local=dict(globals(), **locals()))