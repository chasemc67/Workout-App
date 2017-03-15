import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

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
          self.RockportHRText.config(bg="white")
       except:
          self.RockportHRText.config(bg="red")
          validationSuccess = False

       try:
          float(self.RockportTimeText.get(1.0, tk.END).strip())
          self.RockportTimeText.config(bg="white")
       except:
          self.RockportTimeText.config(bg="red")
          validationSuccess = False

       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.centerFrame = tk.Frame(self)

       self.Rockport = tk.Label(self.centerFrame)
       self.Rockport["text"] = "Rockport 1-Mile Walk"
       self.Rockport.grid(row=0, column=0)

       self.RockportHR = tk.Label(self.centerFrame)
       self.RockportHR["text"] = "Post Test HR: "
       self.RockportHR.grid(row=1, column=0)

       self.RockportHRText = tk.Text(self.centerFrame)
       self.RockportHRText["height"] = 1
       self.RockportHRText["width"] = 5
       self.RockportHRText.bind("<Tab>", self.focus_next_window)
       self.RockportHRText.bind("<Shift-Tab>", self.focus_last_window)
       self.RockportHRText.grid(row=1, column=1)

       self.RockportTime = tk.Label(self.centerFrame)
       self.RockportTime["text"] = "Time(min): "
       self.RockportTime.grid(row=2, column=0)

       self.RockportTimeText = tk.Text(self.centerFrame)
       self.RockportTimeText["height"] = 1
       self.RockportTimeText["width"] = 5
       self.RockportTimeText.bind("<Tab>", self.focus_next_window)
       self.RockportTimeText.bind("<Shift-Tab>", self.focus_last_window)
       self.RockportTimeText.grid(row=2, column=1)

       self.centerFrame.pack()

       self.buttonFrame = tk.Frame(self)
       self.Next = NextButton(self.buttonFrame, controller, self.saveData, self.validateInput)
       self.Next.grid(row=0, column=0)

       self.Back = BackButton(self.buttonFrame, controller)
       self.Back.grid(row=0, column=1)

       self.Quit = QuitButton(self.buttonFrame, controller)
       self.Quit.grid(row=0, column=2)
       self.buttonFrame.pack()

   def loadData(self, person):

       self.RockportHRText.delete(1.0, tk.END)
       self.RockportHRText.insert(tk.END, person.rockportHR)

       self.RockportTimeText.delete(1.0, tk.END)
       self.RockportTimeText.insert(tk.END, person.rockportTime)

   def saveData(self, person):
       person.rockportHR = self.RockportHRText.get(1.0, tk.END).strip()
       person.rockportTime = self.RockportTimeText.get(1.0, tk.END).strip()
