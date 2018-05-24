from tkinter import *
from tkinter import PhotoImage
import time
import vlc



class Pelota:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 50, 50, fill=color)
        self.canvas.move(self.id, 500, 200)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def movePelota(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0


    def left(self, evt):
        self.x = -2

    def right(self, evt):
        self.x = 2


tk = Tk()
tk.title("Futbol")
canvas = Canvas(tk, width=800, height=400)
canvas.pack()
tk.update()
my_image2 = PhotoImage(file='porteria1.gif')
canvas.create_image(0, 100, anchor=NW, image=my_image2)
pelota = Pelota(canvas, 'black')

while 1:
    p = vlc.MediaPlayer("1.mp3")
    p.play()
    pelota.movePelota()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.1)

tk.update()
p.stop()
tk.mainloop()
