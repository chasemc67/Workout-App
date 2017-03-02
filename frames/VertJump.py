import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class VertJump(tk.Frame):
 
   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.VertJumpSRText.get(1.0, tk.END).strip())
          self.VertJumpSRText.config(highlightbackground="white")
       except:
          self.VertJumpSRText.config(highlightbackground="red")
          validationSuccess = False

       try:
          float(self.VertJumpBestText.get(1.0, tk.END).strip())
          self.VertJumpBestText.config(highlightbackground="white")
       except:
          self.VertJumpBestText.config(highlightbackground="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.VertJump = tk.Label(self)
       self.VertJump["text"] = "Vertical Jump"
       self.VertJump.grid(row=0, column=0)

       self.VertJumpSR = tk.Label(self)
       self.VertJumpSR["text"] = "Standing Reach(ft.inch): "
       self.VertJumpSR.grid(row=1, column=0)

       self.VertJumpSRText = tk.Text(self)
       self.VertJumpSRText["height"] = 1
       self.VertJumpSRText["width"] = 5
       self.VertJumpSRText.bind("<Tab>", self.focus_next_window)
       self.VertJumpSRText.bind("<Shift-Tab>", self.focus_last_window)
       self.VertJumpSRText.grid(row=1, column=1)

       self.VertJumpBest = tk.Label(self)
       self.VertJumpBest["text"] = "Best Attempt(ft.inch): "
       self.VertJumpBest.grid(row=2, column=0)

       self.VertJumpBestText = tk.Text(self)
       self.VertJumpBestText["height"] = 1
       self.VertJumpBestText["width"] = 5
       self.VertJumpBestText.bind("<Tab>", self.focus_next_window)
       self.VertJumpBestText.bind("<Shift-Tab>", self.focus_last_window)
       self.VertJumpBestText.grid(row=2, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)

   def loadData(self, person):

       self.VertJumpSRText.delete(1.0, tk.END)
       self.VertJumpSRText.insert(tk.END, person.vertJumpSR)

       self.VertJumpBestText.delete(1.0, tk.END)
       self.VertJumpBestText.insert(tk.END, person.vertJumpBest)

   def saveData(self, person):
       person.vertJumpSR = self.VertJumpSRText.get(1.0, tk.END).strip()
       person.vertJumpBest = self.VertJumpBestText.get(1.0, tk.END).strip()
