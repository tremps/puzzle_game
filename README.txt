Basic desciption of puzzle:
2 windows will open when the game is run. One contains an nxn grid of tiles. The other
contains a row of buttons. Each button can be turned on and off by clicking it. If
a button is turned on, it activates a subset of the tiles. Tiles are yellow by default.
When activated by a single button they turn green. When activated by multiple buttons
they turn red. The goal is to turn on a subset of buttons such that every tile is green.

Use:

1. Generate a board

python3 gen_board.py <grid dimmensions> <number of buttons>

This will create a .board file which stores the data for a puzzle with corresponding
tile grid dimmensions and number of buttons.


2. Include a victory image

Add to this directory an image file named "win.png". This is the image that will be displayed
when the puzzle is solved.


3. Start the puzzle

./run.sh <name of .board file to use>

This opens the 2 windows. For basic use, place them side by side and play. If more than 1 person
will be playing the puzzle, for a greater challenge you can put the 2 windows on different monitors
set up so that they can't both be seen from the same place. This forces group members to only
see 1 part of the puzzle at a time and communicate about what they see.


Final notes:

I recomend only telling players which window can be interacted with/clicked and no
other information about the puzzle. With enough trial and error they should be able
to figure out the rules and goal.

An 8x8 tile grid with 8 buttons seems to be a good difficulty.

Running the puzzle will create a colors.data file which can be deleted once the program ends.