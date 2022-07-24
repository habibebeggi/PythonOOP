from tkinter import *
class Senators:
    def __init__(self):
        window=Tk()
        window.title("Eyaletler Senatörler")
        Label(window, text="Eyalet: ", width=5).grid(row=0, column= 0, sticky= E)
        self.state=StringVar()
        entState=Entry(window, textvariable=self.state)
        entState.grid(row=0,column=1, sticky=W)
        entState.focus_set()
        entState.bind("<Button-1>", self.clearBoxes)
        btnDisplay= Button(text= "Senatörleri Göster", command=self.senate)
        btnDisplay.grid(row=1, columnspan=2, pady=10)
        self.L=[]
        self.listContents=StringVar()
        self.listContents.set(tuple(self.L))
        lstSenators=Listbox(window, height=2, width=21, listvariable=self.listContents)
        lstSenators.grid(row=2, column=0, columnspan=2, padx=44, pady=2)
        window.mainloop()
    def clearBoxes(self, e):
        self.state.set("")
        self.listContents.set(tuple([]))
    def senate(self):
        self.L=[]
        result=self.state.get()
        infile=open("Senate114.txt",'r')
        for line in infile:
            temp=line.split(',')
            if temp[1]==result:
                self.L.append(temp[0]+ " " + temp[2])
                self.listContents.set(tuple(self.L))
        infile.close()
Senators()