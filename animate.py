
## Langton's Ant
## Writen in Python on 11/08/2023
## runner.py

import math
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import ants
import field

# ------------------------------- #
# Langtons Ant is a Two Dimensional Universal Turning Machine with very simple rules
# However these rules have Emergent Behavior. Langton's Ant is described as a 
# Ceullar Automata where the Rid is colored black or white to determine where the Ant has been

# This Script has customizable parameters which can modify the Ants Outcome
# ------------------------------- #

# Run the Simulation of the Langton's Ants
def simulate_ants(grid,length,states,colony):
	# Save Size
	size = (len(grid))
	# Create the Plots
	fig = plt.figure()

	# Create the Animation Frame
	back_anim = plt.imshow(grid,cmap="nipy_spectral",vmin=0,vmax=states,extent=[0,size,0,size])

	# Animate the Sequence
	def animate(i):
		frame = field.update_field(grid,colony)
		back_anim.set_data(frame[0])
		return [back_anim]

	# Run Animation
	anim = animation.FuncAnimation(fig,animate,frames=length,interval=1,blit=True,repeat=False)
	# Save Animation
	anim.save('animation.gif', writer='imagemagick', fps=30)
	# Show Animation
	plt.show()

# Generates Each Frame of the Animation
def generate_frame(grid,frames,colony):
	# Save Size
	size = (len(grid))
	# Snapshots are all the Frames which will be Animated
	back_snapshots = []
	ant_snapshots = []
	# Runs Simulation
	for frame in range(frames):
		# Update the Field
		update = field.update_field(grid,colony)
		# Append the Frame to the list of Frames
		back_snapshots.append(update[0])
		# Create a Mask for Each Ant
		for ant in update[1]:
			ant_display = np.array(field.init(size,size))
			ant_display[ant[0][0]][ant[0][1]] = 1
			ant_snapshots.append(ant_display)
	# Return the Snapshots
	return back_snapshot, ant_snapshot

# ------------------------------- #

# Saved for Testing Purposes
# Simulates the Colony Frame by Frame
def simulate_ants_frame_by_frame(grid,frames,states,colony):
	# Runs Simulation 
	for frame in range(frames):
		# Save Size
		size = (len(grid))
		# Create the Plots
		fig, ax = plt.subplots()
		# Update the Field
		update = field.update_field(grid,colony)
		back_frame = update[0]
		# Create the Background of Resulting Pattern
		img1 = ax.imshow(back_frame, cmap="gray", vmin=0, vmax=states, extent=[0,size,0,size])
		# Display Each Ant in the Colony
		for ant in update[1]:
			display = np.array(field.init(size,size))
			display[ant[0][0]][ant[0][1]] = 1
			show = np.ma.masked_array(display, display <= 0)
			new_image = ax.imshow(show, cmap=ant[1], extent=[0,size,0,size])
		# Show the Plot
		plt.show()

# ------------------------------- #
