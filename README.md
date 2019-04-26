RockPaperScissors
=================

A Rock - Paper - Scissors (and much more) game made in Python :)

The new goal of this project is to

[+] Fix the old code so that it works, isn't as heavy, and looks nicer
[+] Create save files for individual players
[+] Create a User Interface
	[ ] Give an options menu to: edit the players list, show high scores, change games, choose your AI
[+] Gain massive amounts of data online and use a super computer (Stampede2) to process it
	[ ] Interpret and use the processed data
[ ] Find a nice way to work with the elements of the rock, paper, scissors game. Maybe make the elements a subclass or a seperate class. Or make a successor function.
[ ] Create an AI which can predict human behavior of rock, paper, scissors
[ ] Create a way to test the AI. Perhaps a fitness function.
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


Future Ideas for a full game:
Download player data from 10,000 human games of rock paper scissors.
The player fights enemies by playing RPS. If you loose a round you loose health. The player and the enemy have health bars.
Have everything about the game designed to lull the player into a pattern: upgrades to make certain moves stronger or provide more defence, upgrades to make certain combinations even stronger (using rock twice in a row dose double damage the second time), have a count down timer to that there isn't too much time to think each round (this will also make people want to play more rounds), have 8-bit music which provides a different note/sound for each element you choose (also a sound effect for winning or loosing).


AI Ideas:
Humans really don't like to give "random" data with too many percieved patterns. So they will be more likely to not choose rock after choosing rock 2 or 3 tiems in a row. Look for the higher expectation value, not nessisarily the one that will win.