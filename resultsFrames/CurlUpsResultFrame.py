import tkinter as tk

class CurlUpsResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1
        self.CurlUpLabel = tk.Label(self)
        self.CurlUpLabel["text"] = "10cm Curl Ups"
        self.CurlUpLabel.grid(row=0, column=0)

        self.CurlUpNumLabel = tk.Label(self)
        self.CurlUpNumLabel["text"] = ("Number: " + person.curlUpNum)
        self.CurlUpNumLabel.grid(row=self.row, column=0)
        self.row += 1
