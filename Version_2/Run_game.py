import UIs 
from UIs import Default_UI as UI
from UIs import Fantasy_skin as UI2
from UIs import Fantasy_skin2 as UI3

def Run_game(UI):
	"This is the architecture of the whole game"
	UI.Setup()
	UI.Welcome()
	UI.Game_intro()
	UI.Game_play()
	UI.Save_data()
	UI.Goodbye()

Run_game(UI3)