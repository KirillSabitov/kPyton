from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()

def extrtmlkjk():
    file_name = fd.askopenfilename()
    filett=(("TXT files", "*.txt"),
            ("HTML files",))