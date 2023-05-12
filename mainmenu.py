"""
Funky game moment, idk this is just a game I made in my free time, coz I got bored lol
"""
import game as game
import os
import sys
from pathlib import Path
import csv


class NewFileData:
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
    player_inventory = []
    player_equipment = []
    player_skills = []
    player_spells = []
    player_location = []
    player_quests = []
    player_achievements = []
    player_deaths = 0
    player_wins = 0
    player_losses = 0
    player_total_battles = 0
    player_total_damage_dealt = 0
    player_total_damage_taken = 0
    player_total_healing_done = 0
    player_total_healing_taken = 0
    player_total_critical_hits = 0
    player_total_critical_misses = 0
    player_total_dodges = 0
    player_total_misses = 0
    player_total_blocks = 0
    player_total_turns = 0
    player_total_time_played = 0
    player_total_time_afk = 0
    player_total_time_online = 0
    player_total_time_offline = 0
    player_total_time_dead = 0
    player_total_time_alive = 0
    player_total_time_in_combat = 0
    player_total_time_out_of_combat = 0

    datalist = [player_lvl, player_xp, player_hp, player_mp, player_attack, player_defense, player_magic_attack,
                player_magic_defense, player_speed, player_luck, player_gold, player_inventory, player_equipment,
                player_skills, player_spells, player_location, player_quests, player_achievements, player_deaths,
                player_wins, player_losses, player_total_battles, player_total_damage_dealt, player_total_damage_taken,
                player_total_healing_done, player_total_healing_taken, player_total_critical_hits,
                player_total_critical_misses, player_total_dodges, player_total_misses, player_total_blocks,
                player_total_turns, player_total_time_played, player_total_time_afk, player_total_time_online,
                player_total_time_offline, player_total_time_dead, player_total_time_alive, player_total_time_in_combat,
                player_total_time_out_of_combat]


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
        self.filename = ""

    def input_gathering(self):
        self.playerName = input("Enter your name: ")
        self.file_creation(self)

    def file_creation(self):
        self.filename = Path("saves/" + self.playerName + ".csv")
        datalist = NewFileData.datalist
        datalist.insert(0, self.playerName)
        with open(self.filename, "a") as f:
            writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(datalist)

        LoadGame.read_save(self=LoadGame, newSave=self.filename)


class LoadGame(MainMenu):
    def __init__(self):
        super().__init__()
        self.allSaves = []
        self.save = ""

    # Function for selecting save files
    def select_save(self):
        print("Available saves:")
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
        with open(filepath, "r") as f:
            reader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            saveData = list(reader)
            os.system('cls||clear')
            game.MainGame.__init__(self=game.MainGame, saveData=saveData)

    # Function for grabbing all save files in /saves and printing them to screen with a number
    def grab_saves(self):
        self.allSaves = os.listdir(Path("saves/"))
        self.select_save(self)


if __name__ == "__main__":
    MainMenu.mainMenu(self=MainMenu)
