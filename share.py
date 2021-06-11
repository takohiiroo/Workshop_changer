import os


f_read = open("RocketLeaguePath.txt", "r", encoding="UTF-8")
epic_parent = f_read.read()
f_read.close()

backup_folder = "/rocketleague/TAGame/CookedPCConsole/"
shichu = "Labs_CirclePillars_P.upk"
folder_full_path = epic_parent + backup_folder
full_path = folder_full_path + shichu