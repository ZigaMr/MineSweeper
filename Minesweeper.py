from tkinter import *
import random
from functools import partial

class Minesweeper():

    def __init__(self,master):

        self.st_vrstic = int(input("Stevilo vrstic: "))
        self.st_stolpcev = int(input("Stevilo stolpcev: "))
        
        frame = Frame(master)
        frame.pack()


        self.label1 = Label(frame, text="Minesweeper")
        self.label1.grid(row = 0, column = 0, columnspan = 10)

        self.menu = Menu(master)
        master.config(menu=self.menu)
        self.menu.add_command(label="QUIT", command=root.destroy)
        self.buttons = dict()
        y=0
        num_proximity_mines=0

        for i in range(self.st_vrstic):
            for x in range(self.st_stolpcev):
                mine = 0
                if random.randint(1,10) == 5:
                    mine = 1
                self.buttons[y] = [Button(frame, bg = "green", width=3),
                                   mine,
                                          #command=partial(self.lclick, y, mine)),
                                   num_proximity_mines]
                self.buttons[y][0].bind('<Button-1>', self.lclick(y))
                self.buttons[y][0].bind('<Button-3>', self.rclick(y))
                y+=1
        y=0
        for i in range(self.st_vrstic):
            for x in range(self.st_stolpcev):
                self.buttons[y][0].grid(row = i, column = x)
                y+=1
        for i in range(self.st_vrstic*self.st_stolpcev):
            n=0
            for x in [i-self.st_stolpcev-1,i-self.st_stolpcev, i - self.st_stolpcev+1,i-1,i+1,
                      i+self.st_stolpcev-1, i+self.st_stolpcev, i+self.st_stolpcev+1]:
                try:
                    #If there's a mine
                    if self.buttons[x][1] == 1:
                        n+=1
                except:
                    pass
            self.buttons[i][2]=n

        master.attributes("-topmost", True)

    def lclick(self,y):
        return lambda Button: self.lclick2(self.buttons[y],y)

    def rclick(self,y):
        return lambda Button: self.rclick2(self.buttons[y],y)

    def lclick2(self,sez,y):
        if sez[1] == 1:
            self.buttons[y][0].config(bg="red")
            print("Sorry nigga")
            top = Toplevel()
            top.title("YOU LOSE")

            msg = Message(top, text="LOSER")
            msg.pack()
        else:
            txt = self.buttons[y][2]
            self.buttons[y][0].config(text=str(txt))


    def rclick2(self,sez,y):
        self.buttons[y][0].config(bg="yellow", text=":)")
root = Tk()
minesweeper = Minesweeper(root)
root.mainloop()
        

    
    
