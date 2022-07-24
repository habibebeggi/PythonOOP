from tkinter import *
class PlaceManagerDemo:
    def __init__(self):
        window=Tk()
        window.title("Koordinat Konumlandırma")
        Label(window, text = " M A V İ", fg = "dark red", bg="light blue").place(x = 50, y = 50)
        Label(window, text = "K K U", fg = "brown", bg="yellow").place(x = 50, y = 100)
        Label(window, text = "K İ T A P",fg = "black", bg = "light green").place(x = 50, y = 150)
        window.mainloop()
PlaceManagerDemo()