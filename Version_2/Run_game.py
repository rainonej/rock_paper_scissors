import UIs 
from UIs import Default_UI as UI

def Run_game(UI):
	"This is the architecture of the whole game"
	UI.Welcome()
	UI.Game_intro()
	UI.Game_play()
	UI.Save_data()
	UI.Goodbye()

Run_game(UI)