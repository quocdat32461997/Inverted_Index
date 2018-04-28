from inverted_index import word_index
from inverted_table import table
from tkinter import *
from D:\inverted_index\venv\Lib\site-packages import wx
from tkinter import messagebox
global tab
tab = table()
print(sys.path)
tab.create_inverted_table('text.txt')
tab.create_inverted_table('text11.txt')

root = Tk()
class myApp(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("First GUI")
        self.pack(fill=BOTH, expand=1)
        textBox = Text(self, height = 2, width = 10)
        textBox.pack()
        quitButton = Button(self, text="Quit", command = self.client_exit)
        quitButton.place(x=0, y=0)
        searchButton = Button(self, text="Search", command = lambda : tab.print_table(textBox.get("1.0","end-1c")))
        searchButton.pack(side=BOTTOM)

    def client_exit(self):
        exit()

    def print_table(self, word):
        w = tab.ivnerted_table[tab.find(word)]
        word_table = w.lsit_file
        print("Table of " + w.get_word() + " :")
        for element in word_table.keys():
            print(element, end="  ")
            print(word_table[element])

root.geometry("400x300")
app = myApp(root)
root.mainloop()


#tab.print_table('Dat')