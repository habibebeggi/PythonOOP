from tkinter import *
class EnlargeShrinkCircle:
    def __init__(self):
        self.radius=50
        window=Tk()
        window.title("Çember Daralıyor Genişliyor")
        self.canvas = Canvas(window, bg = "light blue", width = 300, height = 200)
        self.canvas.pack()
        self.canvas.create_oval(100 - self.radius, 100 - self.radius, 100 + self.radius, 100 + self.radius)
        self.canvas.bind("<Button-1>",self.increaseCircle)
        self.canvas.bind("<Button-3>", self.decreaseCircle)
        window.mainloop()
    def increaseCircle(self, event):
        self.canvas.delete("oval")
        if self.radius < 100:
            self.radius += 4
        self.canvas.create_oval(100-self.radius, 100-self.radius, 100+self.radius, 100+self.radius)
    def decreaseCircle(self, event):
        self.canvas.delete("oval")
        if self.radius > 2:
            self.radius -=4
        self.canvas.create_oval(100- self.radius, 100 - self.radius, 100+ self.radius, 100- self.radius)
EnlargeShrinkCircle()
