# Accepts list of visited coords and maze as input
# Outputs maze with solution path indicated
class MazePlotter:

    def __init__(self, maze_map, visited_coords):
        self.maze = maze_map
        self.visited_coords = visited_coords

    def perform(self):

        if not self.visited_coords:
            return
        solution_indices = self._indexify_coords(self.visited_coords)
        
        solved_maze = self._plot_to_maze(self.maze, solution_indices)
        self._print_to_file(solved_maze)
        return

    """Private methods"""
    def _indexify_coords(self, visited_coords):
        coord_indexifier = lambda xy: (xy[0]-1, xy[1]-1)
        indexified_coords = [coord_indexifier(coord) for coord in visited_coords]
        return indexified_coords

    def _plot_to_maze(self, maze, indexified_coords):
        output_maze = [list(line) for line in maze]
        for (x, y) in indexified_coords:
            output_maze[y][x] = '.'
        output_maze = [''.join(line) for line in output_maze]
        return output_maze

    def _print_to_file(self, maze):
        for line in maze:
            print(line) #Currently just prints to console
