from tkinter import *
from tkinter import ttk
import os
import glob
import shutil

#Epic Gamesのパスのかかれたtxtを読み込む
f = open("RocketLeaguePath.txt", "r", encoding="UTF-8")
epic_parent = f.read()

backup_folder = "/Epic Games/rocketleague/TAGame/CookedPCConsole/"
shichu = "Labs_CirclePillars_P.upk"
folder_full_path = epic_parent + backup_folder
full_path = folder_full_path + shichu

#backupの存在確認
if not os.path.exists(full_path):
    if os.path.exists(folder_full_path):
        shutil.copy(full_path, full_path + ".backup")
    else:
        import setting



root = Tk()
root.title("Workshop Changer")
frame1 = ttk.Frame(root, padding = 16)
frame1.pack()

#各マップのフォルダーの名前を取得しmap_namesに代入
map_folder = "./Maps"
map_names = os.listdir(map_folder)
v = StringVar(value=map_names)
"""maps_image = []
for x in range(len(maps)):
    folder_name = maps[x]
    picture_name = glob.glob("./Maps/{}/*jpg".format(folder_name))
    maps_image[x] = PhotoImage(file = picture_name[0])"""

#listboxの作成と設置
lb = Listbox(frame1, listvariable=v, selectmode="single", height=4, width=50)
lb.pack(side=TOP)

#置換ボタンと元に戻すボタンを作成
button_change = ttk.Button(frame1, text = "マップ置換")
button_return = ttk.Button(frame1, text = "元に戻す")

#ボタンの設置
button_change.pack(side=LEFT)
button_return.pack(side=RIGHT)

root.mainloop()