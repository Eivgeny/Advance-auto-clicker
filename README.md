# Advance-auto-clicker
<br>
An idea of mine to create auto clicker that can record several mouse clicks that need to be done,
and then run them all by checking the pixel color of the mouse position.

The program starts with 2 options in the main menu:

1. 'r' for recording.
2. 'a' for action.

#recording option:

When the user hit 'm' it saves the current position of the mouse. 
example: ' 917,418 '

then waits till the user hit 'f'.
after the user hits 'f' the program record the new position of the mouse and the pixel color of it
and saves it to the file with the first position. 
example: ' m,917,418,252,252,252,1229,169 '

now the user has the option to exit the recording proses or to continue recording the next mouse click

#run option:

after the user has recorded all the mouse clicks and the pixel color that need to match
the user can hit 'a' (action) in the main menu and the auto clicker will start to run.
it will check one by one of the records:
first it will check if the pixel color matches the color that written to the file.
if it not it will wait and check again after delay.
if matches it will click the mouse in the exact position that has been set and continue to the
next record.
when it finishes the list it will repeat all the records again till the user closes the program.

##### the main goal ####
bot(runs automated tasks)
for childhood multiplayer game that record the movement that needs to be done and run them repeatedly to collect resources.




