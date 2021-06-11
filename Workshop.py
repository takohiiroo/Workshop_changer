from tkinter import *
from tkinter import ttk
import shutil
from typing import Sized
from share import *
import os
import glob
import time

# backupファイルの存在確認
def backup_check():
    global epic_parent
    global folder_full_path
    global full_path
    if not os.path.exists(full_path + ".backup"): # backupがなければ
        if os.path.exists(full_path): # 支柱があれば
            shutil.copy(full_path, full_path + ".backup") # backupを作る
        else: # 支柱さえなければパスが間違っているのでsettingで再設定
            import setting 

            # backup_checkがおわったらpathを更新するために再度txtを読み込み、代入しなおす。
            

            f_read = open("RocketLeaguePath.txt", "r", encoding="UTF-8")
            epic_parent = f_read.read()
            f_read.close()
            folder_full_path = epic_parent + backup_folder
            full_path = folder_full_path + shichu


# 置換ボタンを押したときの動作
def change_map():
    if not os.path.exists(full_path + ".backup"):
        caution.set("ゲームの場所を示すパスが間違っています。再起動して設定しなおしてください。")
        lb.pack_forget()
        button_change.pack_forget()
        button_return.pack_forget()
    else:
        i = lb.curselection() # セレクトされているファイルのインデックスをiに代入
        selected_map_list = glob.glob("./Maps/" + lb.get(i) +"/*udk") # i番目のファイルの中のudkファイルを抽出
        selected_map = "".join(selected_map_list)
        shutil.copy(selected_map, full_path) # カスタムマップを支柱にコピー
        caution.set(lb.get(i) + "に置換しました")
  

def default_map():
    if not os.path.exists(full_path + ".backup"):
        caution.set("ゲームの場所を示すパスが間違っています。再起動して設定しなおしてください。")
        lb.pack_forget()
        button_change.pack_forget()
        button_return.pack_forget()
    else:
        shutil.copy(full_path + ".backup", full_path)
        caution.set("元に戻しました。")
        


#---ここから命令----    
backup_check()

root = Tk()
root.title("Workshop Changer for Epic")
frame1 = ttk.Frame(root, padding = 16)
frame1.pack()


# 各マップのフォルダーの名前を取得しmap_namesに代入
map_folder = "./Maps"
map_names = os.listdir(map_folder)
map_list = StringVar(value=map_names)

caution = StringVar()
caution.set("")
label1 = ttk.Label(
    frame1,
    textvariable=caution,
)
label1.pack(side=TOP)

# listboxの作成と設置
lb = Listbox(
    frame1,
    listvariable=map_list,
    selectmode="single",
    height=4,
    width=50)
lb.pack(side=TOP)

# 置換ボタンと元に戻すボタンを作成
button_change = ttk.Button(
    frame1,
    text = "マップ置換",
    command=change_map
    )

button_return = ttk.Button(
    frame1,
    text="元に戻す",
    command=default_map
    )

#ボタンの設置
button_change.pack(side=LEFT)
button_return.pack(side=RIGHT)

root.mainloop()