import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class WallSlide(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.WallSlideRateText.get(1.0, tk.END).strip())
          self.WallSlideRateText.config(highlightbackground="white")
       except:
          self.WallSlideRateText.config(highlightbackground="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.WallSlide = tk.Label(self)
       self.WallSlide["text"] = "Wall Slide"
       self.WallSlide.grid(row=0,column=0)

       self.WallSlideRate = tk.Label(self)
       self.WallSlideRate["text"] = "Rating(0-3): "
       self.WallSlideRate.grid(row=1, column=0)

       self.WallSlideRateText = tk.Text(self)
       self.WallSlideRateText["height"] = 1
       self.WallSlideRateText["width"] = 5
       self.WallSlideRateText.bind("<Tab>", self.focus_next_window)
       self.WallSlideRateText.bind("<Shift-Tab>", self.focus_last_window)
       self.WallSlideRateText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.WallSlideRateText.delete(1.0, tk.END)
       self.WallSlideRateText.insert(tk.END, person.wallSlideRate)

   def saveData(self, person):
       person.wallSlideRate = self.WallSlideRateText.get(1.0, tk.END).strip()
