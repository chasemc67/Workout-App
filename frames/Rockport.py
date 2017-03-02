import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class Rockport(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.RockportHRText.get(1.0, tk.END).strip())
          self.RockportHRText.config(highlightbackground="white")
       except:
          self.RockportHRText.config(highlightbackground="red")
          validationSuccess = False

       try:
          float(self.RockportTimeText.get(1.0, tk.END).strip())
          self.RockportTimeText.config(highlightbackground="white")
       except:
          self.RockportTimeText.config(highlightbackground="red")
          validationSuccess = False

       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Rockport = tk.Label(self)
       self.Rockport["text"] = "Rockport 1-Mile Walk"
       self.Rockport.grid(row=0, column=0)

       self.RockportHR = tk.Label(self)
       self.RockportHR["text"] = "Post Test HR: "
       self.RockportHR.grid(row=1, column=0)

       self.RockportHRText = tk.Text(self)
       self.RockportHRText["height"] = 1
       self.RockportHRText["width"] = 5
       self.RockportHRText.bind("<Tab>", self.focus_next_window)
       self.RockportHRText.bind("<Shift-Tab>", self.focus_last_window)
       self.RockportHRText.grid(row=1, column=1)

       self.RockportTime = tk.Label(self)
       self.RockportTime["text"] = "Time(min): "
       self.RockportTime.grid(row=2, column=0)

       self.RockportTimeText = tk.Text(self)
       self.RockportTimeText["height"] = 1
       self.RockportTimeText["width"] = 5
       self.RockportTimeText.bind("<Tab>", self.focus_next_window)
       self.RockportTimeText.bind("<Shift-Tab>", self.focus_last_window)
       self.RockportTimeText.grid(row=2, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)

   def loadData(self, person):

       self.RockportHRText.delete(1.0, tk.END)
       self.RockportHRText.insert(tk.END, person.rockportHR)

       self.RockportTimeText.delete(1.0, tk.END)
       self.RockportTimeText.insert(tk.END, person.rockportTime)

   def saveData(self, person):
       person.rockportHR = self.RockportHRText.get(1.0, tk.END).strip()
       person.rockportTime = self.RockportTimeText.get(1.0, tk.END).strip()
