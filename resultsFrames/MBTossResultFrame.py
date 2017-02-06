import tkinter as tk

class MBTossResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1

        self.MBTossLabel = tk.Label(self)
        self.MBTossLabel["text"] = "Med. Ball Toss"
        self.MBTossLabel.grid(row=0, column=0)

        self.MBTossDistLabel = tk.Label(self)
        self.MBTossDistLabel["text"] = ("Throw Distance(cm): " + person.seatMBDist)
        self.MBTossDistLabel.grid(row=self.row, column=0)
        self.row += 1
