from tkinter import *
from tkinter import filedialog
import time
import Main
import subprocess, time, os, sys

class Gui:
    def __init__(self, root):
        self.tk = root
        self.filepath = ""
        self.fileselectbutton = Button(text="select a json", width=30, command=self.getFileName)
        self.fileselectbutton.pack()

        #self.slangbutton = Button(tk, text="misspelling/slang ranking", command=self.getslang)
        #self.slangbutton = Button(tk, text="misspelling/slang ranking")
        #self.slangbutton.pack()
        #self.slangbutton.after(7000, self.getslang)

    def getFileName(self):
        self.filepath = filedialog.askopenfilename()
        #print(self.filepath)
        if self.filepath is not "":
            self.fileselectbutton.destroy()

    def getslang(self):
        if self.filepath is "":
            time.sleep(10)
        words.main(self.filepath)

 

def run_mains():
    Main.main()
    cmd = ["ls", "-la"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in proc.stdout.readlines():
        print(line)
    
tk = Tk()
tk.geometry("500x500")
g = Gui(tk)
tk.after(5000, run_mains)


tk.mainloop()


#canvas_height=20
#canvas_width=200
#y = int(canvas_height / 2) 
#w.create_line(0, y, canvas_width, y ) 
