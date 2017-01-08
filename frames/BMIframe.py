import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class BMIframe(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.BMIresultLabel = tk.Label(self)
       self.BMIresultLabel["text"] = "BMI"
       self.BMIresultLabel.grid(row=1, column=0)

       self.BMIresultText = tk.Text(self)
       self.BMIresultText["height"] = 1
       self.BMIresultText["width"] = 5
       self.BMIresultText.grid(row=1, column=1)

       # make sure to give a saveData function to the nextButton
       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   # example function to be passed to nextButton, giving instrctions
   # for how to save data when next button clicked
   def saveData(self, person):
      person.height = self.BMIresultText.get(1.0, tk.END)
      #print("saved " + person.height + " to person.height")

   # example function called when frame is rendered onto the screen
   # to load up data incase user has already entered data for person
   def loadData(self, person):
      #print("loading data for BMI frame")
      #print("height: " + person.height)
      if person.height != "":
        #print("inserting text " + person.height)    
        self.BMIresultText.delete(1.0, tk.END)
        self.BMIresultText.insert(END, person.height)
