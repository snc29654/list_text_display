### インポート
import tkinter
import glob
from tkinter import *
from PIL import ImageTk, Image
import os
import sys
import time
import tkinter
from PIL import Image, ImageTk
import threading
import time
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import shutil
import os
import glob
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from tkinter import font
import tkinter.font as tkFont
        
from chardet import detect 

encode_type="utf-8"

#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        self.index_before = 0
        self.sizerate=10
        self.n_old=[]
        self.angle=0
        self.filenames =[]
        

        button3= Button(root_main, text=u'ファイル   選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=100, y=30) 




        #文字色、背景色、サイズ、フォントを指定。
        font1 = font.Font(family='Helvetica', size=12, weight='bold')

        label4 = tkinter.Label(root_main, text="Fontサイズ", fg="red", bg="white", font=font1)
        label4.pack(side="top")
        label4.place(x=600, y=100) 

        label5 = tkinter.Label(root_main, text="エンコード", fg="red", bg="white", font=font1)
        label5.pack(side="top")
        label5.place(x=600, y=60) 



    def button3_clicked(self):  
        global encode_type
        self.encode_type=combo.get()
        self.font_size=combo1.get()
        
        #self.sizerate = txt4.get();


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Text file", ".txt")], initialdir=iDir)
        print(self.filenames)
        self.text_box = tk.Text(bg="#000", fg="#fff", insertbackground="#fff",
                   height=30)
        self.text_box.pack()
        self.text_box.place(x=20, y=150)
        fontExample = tkFont.Font(family="Courier", size=self.font_size, weight="normal", slant="roman")

        self.text_box.configure(font=fontExample)


        for name in self.filenames:

            with open(name, 'rb') as f:  # バイナリファイルとしてファイルをオープン
                b = f.read()  # ファイルの内容を全て読み込む

            enc = detect(b)
            self.encode_type=enc['encoding']
            with open(name,encoding=self.encode_type) as f:


                lines = f.readlines()
                for line in lines:
                    print(line, end='')
                    self.text_box.insert(END, line)


        button9 = tk.Button(root_main, text = 'ファイル書き込み', command=self.textwrite)
        button9.place(x=100, y=70) 

        #self.quit()


    def quit(self):
        root_main.destroy()

 



    def textwrite(self):
        get_data=self.text_box.get("1.0", "end")
        print(get_data)
        
        for name in self.filenames:

            out_file=name
            fout_utf = open(out_file, 'w', encoding=self.encode_type)
 
            for row in get_data:
                fout_utf.write(row)
 
        fout_utf.close()



root_main= tkinter.Tk()  
c=image_gui(root_main)  
root_main.title("rootです")  
root_main.geometry("1200x700") 



combo = ttk.Combobox(root_main, state='readonly')
# リストの値を設定
combo["values"] = ("utf-8","shift_jis","euc_jp")
# デフォルトの値を食費(index=0)に設定
combo.current(0)
# コンボボックスの配置
combo.place(x=700, y=60)
#combo.pack()

combo1 = ttk.Combobox(root_main, state='readonly')
# リストの値を設定
combo1["values"] = (8,9,10,11,12,14,16,18,20)
# デフォルトの値を食費(index=0)に設定
combo1.current(0)
# コンボボックスの配置
combo1.place(x=700, y=100)
#combo1.pack()





root_main.mainloop()


    
