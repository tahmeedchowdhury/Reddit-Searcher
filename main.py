import praw
import json
import tkinter as tk
from tkinter import *
from scrape import scraper

class Gui:

    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        root.title("Reddit Searcher")
        self.bg = PhotoImage(file="bgr.png")
        self.bglabel = Label(self.root, image=self.bg)
        self.sublabel = Label(self.root, text="Subreddit Name: ")
        self.wordlabel = Label(self.root, text="Search for: ")
        self.limitlabel = Label(self.root,text="# of Posts: ")
        self.button = Button(root, text="Find", activebackground="blue")
        self.button.bind('<Button-1>',self.onClick)
        self.entry = Entry(self.root)
        self.entry2 = Entry(self.root)
        self.limitentry = Entry(self.root)
        self.button.place(x=180, y=250)
        self.bglabel.place(x=0,y=0)
        self.entry.place(x=135, y=150)
        self.entry2.place(x=135,y=180)
        self.limitentry.place(x=135, y=210)
        self.sublabel.place(x=40,y=150)
        self.wordlabel.place(x=70,y=178)
        self.limitlabel.place(x=70, y=209)
    
    def onClick(self,event):
        window = Toplevel(self.root)
        window.geometry("670x500")
        x = scraper()
        res = x.search(self.entry.get(),self.entry2.get(),int(self.limitentry.get()))
        self.text = Text(window, borderwidth=0, relief=SUNKEN)
        self.text.insert(INSERT,res)
        self.text.place(x=0,y=0)



root = tk.Tk()
gui = Gui(root)
root.mainloop()