from tkinter import *
from tkinter import ttk
import os
import glob

root = Tk()
root.title("Workshop Changer")

frame1 = ttk.Frame(root, padding = 16)
frame1.pack()

#RLのpathがあってるか確認
print(os.path.exists())

#backupの確認

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