from tkinter import *
class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()
        window.title("Event Demo")
        canvas= Canvas(window, bg ="light blue", width=200, height =100)
        canvas.pack()
        canvas.bind("<Button-1>", self.processMouseEvent)
        canvas.bind("<Key>",self.processKeyEvent)
        canvas.focus_set()
        window.mainloop()
    def processMouseEvent(self, event):
        print("Tıklandı:", event.x, event.y)
        print("Ekrandaki konumu", event.x_root, event.y_root)
        print("Hangi butona tıklandı? ", event.num)
    def processKeyEvent(self, event):
        print("Anahtar? ", event.keysym)
        print("Karakter? ", event.char)
        print("Anahtar Kodu? ", event.keycode)
MouseKeyEventDemo()