from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#参照ボタン押した後の設定
def dirdialog_clicked():
    dir_path = filedialog.askdirectory()
    entry1.set(dir_path)

#変更押した後の設定
def change():
    new_path = entry1.get()
    if new_path.rsplit("/", 1)[1] == "Epic Games" :
        print("Yes")
    else:
        print("no")
    

#Epic Gamesフォルダがある場所の書かれたtxtを読み込む
f = open("RocketLeaguePath.txt", "r", encoding="UTF-8")
epic_parent = f.read()

root = Tk()
root.title("setting")
frame1 = ttk.Frame(root, padding = 16)
frame1.pack()

caution = "ロケットリーグのゲームフォルダを読み込めませんでした。。\n rocketleagueフォルダが入っているEpic Gamesフォルダを選択してください。"


text = StringVar()
text.set(caution)
label1 = ttk.Label(
    frame1,
    textvariable = text,
)
label1.pack(side = TOP)

entry1 = StringVar()
entry1.set(epic_parent + "/Epic Games")
path_entry = ttk.Entry(
    frame1,
    textvariable=entry1,
    width=50
    )
path_entry.pack(side=LEFT)

sansho_button = ttk.Button(
    frame1,
    text= "参照...",
    command=dirdialog_clicked,
)
sansho_button.pack(side=LEFT)

change_button = ttk.Button(
    frame1,
    text = "変更",
    command=change
)
change_button.pack()
root.mainloop()