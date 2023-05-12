import mainmenu as mm
import time
import threading
import asyncio
import os


class GameUpdate:
    def __init__(self):
        self.timePlayed = mm.NewFileData.player_total_time_played

    def update(self):
        self.timePlayed += 5


class Tick(GameUpdate):
    def __init__(self):
        super().__init__(self)

    async def tick(self):
        while True:
            time.sleep(5)
            self.update(self)


class MainGame(Tick):
    def __init__(self, saveData):
        super().__init__(self)
        self.saveData = saveData
        self.playerName = saveData[0][0]
        self.playerInventory = saveData[0][12]
        tick = threading.Thread(target=asyncio.run, args=(self.tick(self),))
        tick.start()
        MainGame.game(self)

    def game(self):
        input(f"Welcome {self.playerName}, to the mystical land of Hyrule. You have been chosen by fate to embark on "
              f"a grand quest to save our beloved kingdom from the clutches of evil. A dark force has arisen and "
              f"threatens to engulf the land in shadow. It is up to you to gather the power and courage to face this "
              f"darkness head-on and restore peace to Hyrule. Your journey will be filled with perilous challenges "
              f"and wondrous discoveries, as you explore vast lands, uncover ancient secrets, and forge alliances "
              f"with legendary heroes. The fate of Hyrule rests in your hands. Will you answer the call of destiny "
              f"and become a hero for the ages? (Enter is to continue...)")
        os.system('cls||clear')
        input("You wake up in a small, dimly lit room. You have no memory of how you got here, or even who you are. ")
        os.system('cls||clear')
        input("You look around the room and see a small table with a candle on it. The candle is lit, but the flame "
              "is very small. You can barely see anything in the room. ")
        os.system('cls||clear')
        input("You get up and walk over to the table. You see a small piece of paper on the table. You pick it up and "
              "read it. ")
        os.system('cls||clear')
        input("The paper reads: ")
        input("Hello, if you are reading this, then you must be the one I have been waiting for. I am the King of "
              "Hyrule, and I have summoned you here to save my kingdom from the forces of darkness. ")
        input("I have been searching for someone like you for a long time. Someone who is brave, strong, and "
              "courageous. Someone who can defeat the evil that threatens to destroy us all. ")
        input("I know you have many questions, but there is no time to answer them now. You must leave this place "
              "immediately and find the Expert Claymore. ")
        input("The Expert Claymore is a legendary sword that was forged by the gods themselves. It is said that "
              "whoever wields this sword will have the power to defeat any enemy. ")
        input("You must find this sword and use it to defeat the evil that threatens to destroy us all. ")
        input("I know this is a lot to take in, but you must hurry. The fate of Hyrule rests in your hands. ")
        input("Good luck, and may the gods be with you. ")
        os.system('cls||clear')


if __name__ == "__main__":
    mm.MainMenu.mainMenu(self=mm.MainMenu)
