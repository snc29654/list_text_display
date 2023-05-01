import tkinter

from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from tkinter import filedialog as tkFileDialog
from PIL import Image, ImageTk
from chardet import detect 
import tkinter.font as tkFont

class image_gui():
    def __init__(self):  
        button= ttk.Button(win, text=u'テキストファイル選択', command=self.file_selected)  
        button.pack() 
        button.place(x=10, y=10) 
        self.font_size=10
    #----------------------------------------
    def select_lb(self,event):
        for i in self.lb.curselection():
            print(self.filenames[i])
            self.prev_image(self.filenames[i])
    #----------------------------------------

    def file_selected(self):  


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Text file", ".txt"), ("python", ".py") ], initialdir=iDir)
        #print(self.filenames[0])
     
 
        txt = StringVar(value=self.filenames)
        self.lb= Listbox(win, listvariable=txt,width=80,height=6)
        self.lb.bind('<<ListboxSelect>>', self.select_lb)
        self.lb.grid(row=0, column=1)
        self.lb.configure(selectmode="extended")
        scrollbar = ttk.Scrollbar(win,orient=VERTICAL,command=self.lb.yview)
        scrollbar.grid(row=0,column=2,sticky=(N,S))

    def prev_image(self,n):



        self.text_box = tk.Text(bg="#000", fg="#fff", insertbackground="#fff",
                   height=20)
        #self.text_box.pack()
        self.text_box.place(x=20, y=200)
        fontExample = tkFont.Font(family="Courier", size=self.font_size, weight="normal", slant="roman")

        self.text_box.configure(font=fontExample)

        #f = open(n, encoding="utf-8")
        #text_data = f.read()

        with open(n, 'rb') as f:  # バイナリファイルとしてファイルをオープン
            b = f.read()  # ファイルの内容を全て読み込む

        enc = detect(b)
        self.encode_type=enc['encoding']



        with open(n,encoding=self.encode_type) as f:


            lines = f.readlines()
            for line in lines:
                #print(line, end='')
                self.text_box.insert(END, line)


win = Tk()
win.title('test')
win.geometry("800x600") 
image_gui() 
 
win.mainloop()
