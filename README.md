# maze_solver
Ascii maze solving algorithm

Objects:
- MazeRunner: - Accepts text file as input
							- Passes file to MazeParser to obtain maze as formatted list of strings, start_coords and end_coords
							- Passes maze to MazeSolver to solve
							- Returns True if solvable
							- Returns False if unsolvable 

- MazeParser:	- Accepts text file as input
							- Returns tuple of (maze as list of strings, start_coords, end_coords) if maze has valid start and endpoints
							- Returns False if maze invalid

- MazeSolver:	-	Accepts maze, start_coords, end_coords as input
							- Moves Crawler object around maze and monitors it's position
							- If Crawler moves more than the total number of squares, maze is deemed unsolvable
							- Returns True if Crawler reaches end_coords
							- Returns False if maze unsolvable

- Crawler:		- Accepts x and y coords, and maze as inputs
							- Moves into next empty space by updating its x and y coords