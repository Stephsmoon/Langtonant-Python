
## Langton's Ant
## Writen in Python on 11/08/2023
## runner.py

import ants
import field
import animate

import random
import argparse

# ------------------------------- #
# Langtons Ant is a Two Dimensional Universal Turning Machine with very simple rules
# However these rules have Emergent Behavior. Langton's Ant is described as a 
# Ceullar Automata where the Rid is colored black or white to determine where the Ant has been

# This Script has customizable parameters which can modify the Ants Outcome
# The Pamaters for this Script Include Size and Multiple Rules
# ------------------------------- #

# Create List of Random Spawns
spawns = []

# Runner Script will Run all other Necessary Files
def runner(size,frames,rulesets,rulecolors):
	# Create the Grid
	grid = field.init(size,size)
	print(f"Grid Created with a size of {size}x{size}")
	
	# Get the Largest Element from Rulesets for the States
	states = len(max(rulesets))

	colony = []
	# Create New Ant for Each Ruleset 
	for index, rule in enumerate(rulesets):
		# Get a Random Spawn and Face
		spawn, face = randomizespawn(spawns,size)
		# Get the Color for the Ant
		color = rulecolors[index]
		# Randomize the Spawn of the Ant
		ant = ants.Ant(spawn,rule,face,color)
		# Append the ant to Ants
		colony.append(ant)
		print(f"Ant with Ruleset {rule} has been created in {color}")

	# Create Animation
	animate.simulate_ants(grid,frames,states,colony)

# ------------------------------- #

def randomizespawn(spawns, size):

	# Get the Mid Cord of the Grid
	mid = int(size/2)
	# Extend the Reach of the Randomize Spawn
	reach = int(((len(spawns) % 5) * 2.5) + 5)

	# Generate a Random Spawn
	spawn = (random.randint(mid-reach,mid+reach),random.randint(mid-reach,mid+reach)) 
	# Regenerate the Spawn until the Spawn no longer Exist
	while spawn in spawns:
		spawn = (random.randint(mid-reach,mid+reach),random.randint(mid-reach,mid+reach)) 

	# Choose a Random Face
	faces = [-90,0,90,180]
	face = random.choice(faces)
	# Return both Randomized Values
	return spawn, face

# Custom Argument for a List of Strings
def rulestolist(arg):
	# Splits the Argument into List
	return arg.split(',')

# ------------------------------- #

# Takes in Arguments which are Processed to Run Code
if __name__ == "__main__":
	# ArgumentParser object
	parser = argparse.ArgumentParser()
 
	# Added Arguments
	parser.add_argument("size", help="An Integer which will dictate the Size of the Field", type=int)
	parser.add_argument("frames", help="An Integer which will determine the Length of the Simulation", type=int)
	parser.add_argument('rules',help="List of Rules for Each Ant, seperated by a comma", type=rulestolist)
	parser.add_argument('colors',help="List of Colors for Each Ant, seperated by a comma", type=rulestolist)

	# Parse the command-line arguments
	args = parser.parse_args()

	# Runs the Runner Scriptœ
	runner(args.size, args.frames, args.rules, args.colors)

# ------------------------------- #
