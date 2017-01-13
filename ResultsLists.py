from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack(fill=BOTH, expand=1)

for i in range(23):
    listbox.insert(END, str(i))

mainloop()
