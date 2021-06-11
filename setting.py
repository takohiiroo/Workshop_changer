from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
from share import *
import os
    

#参照ボタン押した後の設定
def dirdialog_clicked():
    dir_path = filedialog.askdirectory()
    entry1.set(dir_path)

#変更押した後の設定
def change():
    new_path = entry1.get()
    if new_path.rsplit("/", 1)[1] == "Epic Games" : # 参照したものがEpic Gamesで終わっているか確認
        if os.path.exists(new_path + "/rocketleague/TAGame/CookedPCConsole/"): # かつそのEpicGamesのなかに目的のフォルダが存在するか確認。
            f_write =open("RocketLeaguePath.txt", "w") 
            f_write.write(new_path) # txtに新しく参照した場所を記録
            f_write.close()
            shutil.copy(new_path + backup_folder + shichu, new_path + backup_folder + shichu +".backup") # ついでにbackupもつくっちゃう
            text.set("ゲームフォルダの設定が完了しました。")
            sansho_button.pack_forget() # 参照ボタンと変更ボタンを消去
            change_button.pack_forget()
            close_button.pack(side=BOTTOM) # 閉じるボタンを表示
        else:
            text.set("ERROR:参照したEpic Gamesフォルダーは目的のフォルダーではありません。\n設定しなおしてください。")
    else:
        text.set("ERROR:参照の仕方が間違っています。\nEpic Gamesフォルダを選択し、パスの最後がEpic Gamesで終わるようにしてください。")



root = Tk()
root.title("setting")
frame1 = ttk.Frame(root, padding = 16)
frame1.pack()



text = StringVar() #最初の注意書き
text.set("ロケットリーグのゲームフォルダを読み込めませんでした。。\n rocketleagueフォルダが入っているEpic Gamesフォルダを選択してください。")

label1 = ttk.Label( #注意書きを設置
    frame1,
    textvariable = text,
)
label1.pack(side = TOP)

entry1 = StringVar() #　パスを入力するところ
entry1.set(epic_parent) #　現在のtxtに書かれているパスを初期設定

path_entry = ttk.Entry( #　入力欄の設置
    frame1,
    textvariable=entry1,
    width=50
    )
path_entry.pack(side=LEFT)

sansho_button = ttk.Button( #　参照ボタンの設置
    frame1,
    text=("参照..."),
    command=dirdialog_clicked,
)
sansho_button.pack(side=LEFT)

change_button = ttk.Button( # 変更ボタンの設置
    frame1,
    text=("変更"),
    command=change
)
change_button.pack()

close_button = ttk.Button( # 閉じるボタンの設置 最初は見せたくないのでpack()していない。
    frame1,
    text=("閉じる"),
    command=root.destroy
)


root.mainloop()

