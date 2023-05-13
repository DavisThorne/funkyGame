import asyncio
import sqlite3
import threading
import time
import os
from pathlib import Path

import mainmenu as mm


class GameUpdate():
    def __init__(self):
        self.timePlayed = 0

    def update(self):
        pass

    def save_game(self, selfDataList):
        saveName = str(selfDataList[0])
        filename = Path("saves/" + saveName + ".db")
        conn = sqlite3.connect(filename)
        conn.execute(f"""UPDATE game_data
                         SET current_level = {selfDataList[1]},
                             health = {selfDataList[2]},
                             mana = {selfDataList[3]},
                             attack_dmg = {selfDataList[4]},
                             defense = {selfDataList[5]},
                             magic_attack_dmg = {selfDataList[6]},
                             magic_defense = {selfDataList[7]},
                             speed = {selfDataList[8]},
                             gold = {selfDataList[9]},
                             total_play_time = {selfDataList[10]}
                         WHERE player_name = '{selfDataList[0]}'""")
        conn.commit()
        conn.close()
        print("Game saved!")


class Tick(GameUpdate):
    def __init__(self):
        super().__init__(self)

    async def tick(self):
        while True:
            time.sleep(5)
            self.update(self)

    async def autoSave(self, saveData):
        while True:
            time.sleep(30)
            self.save_game(self, saveData)


class MainGame(Tick):
    def __init__(self, saveData):
        super().__init__(self)
        self.saveData = saveData
        self.playerName = self.saveData[0]
        self.gold = self.saveData[9]
        tick = threading.Thread(target=asyncio.run, args=(self.tick(self),))
        autosave = threading.Thread(target=asyncio.run, args=(self.autoSave(self, self.saveData),))
        autosave.start()
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
        self.saveData[9] += 100
        print(self.saveData[9])


if __name__ == "__main__":
    mm.MainMenu.mainMenu(self=mm.MainMenu)
