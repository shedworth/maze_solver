from maze_solver import MazeSolver
from maze_parser import MazeParser
from maze_plotter import MazePlotter

class MazeManager:	
    """Manager object that accepts maze as txt file and calls subordinate
    objects to parse maze to a nested list and then solve it."""
    def __init__(self, maze_file):
        self.maze_file = maze_file

    def perform(self):
        parser = MazeParser(self.maze_file)
        #Parser returns Maze named-tuple
        parsed_maze = parser.perform() 
        solver = MazeSolver(parsed_maze)    
        solved_maze_coords = solver.perform()
        if not solved_maze_coords:
            #Solver has failed to solve the maze
            return
        plotter = MazePlotter(parsed_maze.maze_map, solved_maze_coords)
        return plotter.perform()


manager = MazeManager('mazes/maze_pass.txt')
manager.perform()

