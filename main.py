## 参考
# https://qiita.com/SquidSky/items/90eb450310f1697d03e9

import tkinter as tk

def pushed(self):
	self["text"] = "pushed"

root = tk.Tk()
root.title("年賀状TeXスクリプト自動生成")
root.geometry("640x480")

label = tk.Label(root, text="Hello,World")
label.grid()

button = tk.Button(root, text="button", command=lambda:pushed(button))
button.grid()

root.mainloop()