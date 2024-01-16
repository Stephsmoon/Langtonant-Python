
## Langton's Ant
## Writen in Python on 11/08/2023
## display.py

import ants

# ------------------------------- #

# Field can support Multiple Ants but will destroy Ant Objects once they leave the Scene
# Field is a 2D Matrix of Numbers Ranging based on the Max Number of Rules. The Matrix is
# Comprised of Numbers which Dictates the State. After Every Ant has Moved, a List of Cords and Colors
# are saved along with the Updated Grid and sent back.

# ------------------------------- #

# Initalize the Grid
def init(rows,cols):
	# Create the Grid for the Ant
	rows, cols = (rows,cols)
	grid = [[0 for i in range(cols)] for j in range(rows)]
	# Return Grid
	return grid

# Update the Grid Accordingly
def update_field(grid,ants):
	# Create a List of Updated Ant Positions
	show = []
	# Traverse through the List of Ants to Update Each Ant
	for ant in ants: 
		x = ant.cords[0]
		y = ant.cords[1]
		# Push the ant into the Next State	
		grid[x][y] = ant.next_state(grid[x][y])
		# Check whether current Ant has left the Box 
		if ant.cords[0] > len(grid)-1 or ant.cords[1] > len(grid[0])-1:
			# Kill the Object 
			del ant
			continue
		# Grab the Ants Cords to Display the Ant
		show.append((ant.cords,ant.color))
	# Return the Grid
	return (grid,show)

# ------------------------------- #
