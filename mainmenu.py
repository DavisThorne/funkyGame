"""
Funky game moment, idk this is just a game I made in my free time, coz I got bored lol
"""
import game as game
import os
import sys
from pathlib import Path
import csv
import sqlite3


class NewFileData:
    playerName = ""
    player_lvl = 1
    player_xp = 0
    player_hp = 100
    player_mp = 100
    player_attack = 10
    player_defense = 10
    player_magic_attack = 10
    player_magic_defense = 10
    player_speed = 10
    player_luck = 10
    player_gold = 0
    player_total_play_time = 0
    player_inventory = {}

    def data_base_creation(self, saveName, playerName):
        conn = sqlite3.connect(saveName)
        conn.execute('''CREATE TABLE game_data
                     (player_name TEXT NOT NULL,
                     current_level INTEGER NOT NULL,
                     health INTEGER NOT NULL,
                     mana INTEGER NOT NULL,
                     attack_dmg INTEGER NOT NULL,
                     defense INTEGER NOT NULL,
                     magic_attack_dmg INTEGER NOT NULL,
                     magic_defense INTEGER NOT NULL,
                     speed INTEGER NOT NULL,
                     gold INTEGER NOT NULL,
                     total_play_time FLOAT NOT NULL);''')
        conn.commit()
        conn.close()
        print("Database created successfully!")
        self.data_addition(self, saveName, playerName)

    def data_addition(self, saveName, playerName):
        self.playerName = playerName
        conn = sqlite3.connect(saveName)
        conn.execute(f"""INSERT INTO game_data (player_name, current_level, health, mana, attack_dmg, defense, magic_attack_dmg, magic_defense, speed, gold, total_play_time)
                     VALUES ('{self.playerName}', {self.player_lvl}, {self.player_hp}, {self.player_mp}, {self.player_attack}, {self.player_defense}, {self.player_magic_attack}, {self.player_magic_defense}, {self.player_speed}, {self.player_gold}, {self.player_total_play_time});""")
        conn.commit()
        conn.close()
        LoadGame.read_save(self=LoadGame, newSave=saveName)


class MainMenu:
    def __init__(self):
        return

    def mainMenu(self):
        print("Welcome to the main menu!")
        print("1. New Game")
        print("2. Load Game")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system('cls||clear')
            NewGame.input_gathering(self=NewGame)
        elif choice == "2":
            os.system('cls||clear')
            LoadGame.grab_saves(self=LoadGame)
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice!")
            self.mainMenu()


class NewGame(MainMenu):
    def __init__(self):
        super().__init__()
        self.playerName = ""
        self.saveDataFileName = ""
        self.playerInventoryFileName = ""

    def input_gathering(self):
        self.playerName = input("Enter your name: ")
        self.new_save_creation(self)

    def new_save_creation(self):
        self.saveDataFileName = Path("saves/" + self.playerName + ".db")
        NewFileData.data_base_creation(self=NewFileData, saveName=self.saveDataFileName, playerName=self.playerName)


class LoadGame(MainMenu):
    def __init__(self):
        super().__init__()
        self.allSaves = []
        self.save = ""

    # Function for selecting save files
    def select_save(self):
        print("Available saves:")
        # Enumerate all saves in /saves and print them to screen with a number
        for n, s in enumerate(self.allSaves):
            print(f"{n + 1}) {s}")
        choice = input("Enter your choice: ")
        self.save = str(self.allSaves[int(choice) - 1])
        self.read_save(self, newSave=None)

    # Function for reading data from selected save file
    def read_save(self, newSave):
        if newSave is not None:
            filepath = newSave
        elif newSave is None:
            filepath = Path("saves/" + self.save)
        conn = sqlite3.connect(filepath)
        cursor = conn.execute("SELECT * from game_data")
        rows = cursor.fetchall()
        data = list(*rows)
        conn.close()
        game.MainGame.__init__(self=game.MainGame, saveData=data)

    # Function for grabbing all save files in /saves and printing them to screen with a number
    def grab_saves(self):
        self.allSaves = os.listdir(Path("saves/"))
        self.select_save(self)


if __name__ == "__main__":
    MainMenu.mainMenu(self=MainMenu)
