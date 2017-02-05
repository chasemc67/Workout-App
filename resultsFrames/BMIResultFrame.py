import tkinter as tk

class BMIResultFrame(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.BMIresultLabel = tk.Label(self)
       self.BMIresultLabel["text"] = "BMI"
       self.BMIresultLabel.grid(row=1, column=0)

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
