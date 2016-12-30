import tkinter as tk

class CurlUps(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.CurlUp = tk.Label(self)
       self.CurlUp["text"] = "10cm Curl Ups"
       self.CurlUp.grid(row=0, column=0)

       self.CurlUpNum = tk.Label(self)
       self.CurlUpNum["text"] = "Number: "
       self.CurlUpNum.grid(row=1, column=0)

       self.CurlUpNum = tk.Text(self)
       self.CurlUpNum["height"] = 1
       self.CurlUpNum["width"] = 5
       self.CurlUpNum.grid(row=1, column=1)

       self.NextF = tk.Button(self)
       self.NextF["text"] = "Next"
       self.NextF["fg"] = "black"
       self.NextF["command"] = lambda: controller.next_page()
       self.NextF.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitF = tk.Button(self)
       self.QuitF["text"] = "Quit"
       self.QuitF["fg"] = "black"
       self.QuitF["command"] = lambda: controller.show_frame("MainPage")
       self.QuitF.grid(row=2, column=2)