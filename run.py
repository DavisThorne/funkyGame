import mainmenu as mm
from pathlib import Path

filepath = Path("saves/")
if filepath.is_dir() is False:
    filepath.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    mm.MainMenu.mainMenu(self=mm.MainMenu)