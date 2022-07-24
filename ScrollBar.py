from tkinter import *
class ScrollText:
    def __init__(self):
        window=Tk()
        window.title("Kaydırma Çubuğu örneği")
        frame1=Frame(window)
        frame1.pack()
        scrollbar= Scrollbar(frame1)
        scrollbar.pack(side =LEFT, fill= Y)
        text=Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand=scrollbar)
        text.pack()
        text.insert(END, "")
        scrollbar.config(command=text.yview)
        window.mainloop()
ScrollText()