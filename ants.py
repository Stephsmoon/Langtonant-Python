
## Langton's Ant
## Writen in Python on 11/08/2023
## runner.py

import math

# ------------------------------- #

# Ants are created through Objects which dictate their Cords, Faces, and Rules.
# Cords are where Ants are placed in the Field. Faces is what direction the Ant will Face.
# Rules dictate how the Ant Moves based on the Extension of Colors. Usually Langton's Ant
# has only Black and White, however both Greg Turk and Jim Propp considered an extension
# where the ant uses more than just Two Colors.

# Rules are reflected on the Number of Cell States that exist. With 0 being Blank and each
# Number thus being a new color to the Field. From N to 0, Rules are created with each state
# either being R or L. Langton's Ant uses the rules RL. 

# Instead of 2, Ants here have 3 possible Rules. Being Right (R), Left (L), Back (B). 
# Which corresponds as -90°, 90°, and 180°.

# ------------------------------- #

# Ant Object
class Ant:

    # Initializes the Ant with a set of Varibles
    def __init__(self,cords,rules,face,color):
        # Tuple which are the Cords
        self.cords = cords
        # Tuple which contains the Ruleset
        self.rules = rules
        # Number of Steps
        self.steps = 0
        # Degrees in Degrees
        self.face = face
        # Color of the Ant will be on the Field
        self.color = color

    # Destroys the Ant 
    def __del__(self):
        print(self.steps)

    # Function to move the Ant to the Next State
    def next_state(self, cell):
        # Try whether Cell State Exist in Rules
        try: 
            rule = self.rules[cell]
        # Subtract the State by the Length of Rules to Loop the State
        except:
            rule = self.rules[int(cell-len(self.rules))]
        # Switch Statement for the Ruleset 
        if rule == 'R':
            # Change the Face of the Ant, Right
            self.face -= 90
        elif rule == 'L':
            # Change the Face of the Ant, Left
            self.face += 90
        else:
            # Change the Face of the Ant, Back
            self.face += 180
        # Change the Color of the Cell to the Next Color
        if cell < len(self.rules)-1:
            # Cell is Directly Changed
            cell += 1
        else:
            # Set Cell back to Zero 
            cell = 0 
        # Update the Cell the Ant is on
        self.cords = (self.cords[0] + (int(math.sin(math.radians(self.face)))),self.cords[1] + (int(math.cos(math.radians(self.face))))) 
        # Update the Steps Made
        self.steps += 1
        # Return the Cell
        return cell 

# ------------------------------- #
