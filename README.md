# Challenge 002 : Langtonantpy

The given challenge was to "Create Langton's Ant with an extension to Multiple Colors which can be modified and displayed through a window in Python".

The Lantonantpy project is a program which takes multiple arguments which could create mutliple Ants which could have multiple rules. These inputs come from arguments when running the runner.py file. The runner.py file runs all the necessary code to start the simulation of Langton's Ants. This simulation is displayed through Matlibplot Animations. 

There is an issue with the Animated Display since Multiple Mask could not be configured properly to work with the Animation, meaning that there are no colors for Multiple Ants.

## Compiling and Running

The Project has already been compiled; this project does require multiple packages to run.

```bash
pip3 install -r requirements.txt
```

Although the program can be runned through the terminal through the following command. This will require multiple arguments. Size dictates the size of the field. Frames dictates how many frames will be shown through the simulation. Rules can be described as R (Right), L (Left), and B (Back); these rules can be put together to create ruleset for the the Ants. You can also declare multiple rules: RLBL,RLLR. Colors dictates what colors will be used for each ruleset. This works in frame by frame but not for the full animation. 

```bash
python3 runner.py [size] [frames] [rules] [colors]
```

## Resources

Resources that where used included my Notes from my Cellular Automata Project along with the Wikipedia Page for Langton's Ant. This Project was originally done in a day although was further edited over a month. 

[Langtons Ant](https://en.wikipedia.org/wiki/Langton%27s_ant)
