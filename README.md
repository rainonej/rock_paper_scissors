RockPaperScissors
=================

A Rock - Paper - Scissors (and much more) game made in Python :)

The new goal of this project is to

[ ] Fix the old code so that it works, isn't as heavy, and looks nicer
[ ] Create an AI which can predict human behavior of rock, paper, scissors
[ ] Create a Graphical User Interface for the game


Fixing the old code:
a) I need to create a seperate file for all the functions
b) Make sure there is an easy way out from anywhere in the program
c) I feel like there should be a class here somewhere
d) I need to create/write some file which stores all the past rock, paper, scissors data

a) 
Make a RockPaperScissors class which consists of a list of all the elements of the game and all the winning combinations 
(if two elements aren't in a winning pair then it's assumed a tie, if they are then we check who won). 
It will also have attributes of text that will be spit out at certain times (like the rules of the game or different whatever). 
We should have a player class with a player history, wlt record, and an optional name. 
For now the "AI" will just be a random number generator, but in the future it will be an AI. There will 
There should also be a file thats created/updated everytime a game is finished or the program is editted that keeps the players history and the wlt record.