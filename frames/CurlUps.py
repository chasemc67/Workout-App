import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class CurlUps(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.CurlUp = tk.Label(self)
       self.CurlUp["text"] = "10cm Curl Ups"
       self.CurlUp.grid(row=0, column=0)

       self.CurlUpNum = tk.Label(self)
       self.CurlUpNum["text"] = "Number: "
       self.CurlUpNum.grid(row=1, column=0)

       self.CurlUpNumText = tk.Text(self)
       self.CurlUpNumText["height"] = 1
       self.CurlUpNumText["width"] = 5
       self.CurlUpNumText.bind("<Tab>", self.focus_next_window)
       self.CurlUpNumText.bind("<Shift-Tab>", self.focus_last_window)
       self.CurlUpNumText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):
       self.CurlUpNumText.delete(1.0, tk.END)
       self.CurlUpNumText.insert(tk.END, person.curlUpNum)

   def saveData(self, person):
       person.curlUpNum = self.CurlUpNumText.get(1.0, tk.END)
