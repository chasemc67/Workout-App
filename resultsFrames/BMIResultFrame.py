import tkinter as tk

class BMIResultFrame(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.BMIresult = tk.Label(self)
       self.BMIresult["text"] = ("BMI: " + str(self.controller.person.getBMI()))
       #self.BMIresult["text"] = ("BMI: " + "100")
       
       self.BMIresult.pack()

   # example function to be passed to nextButton, giving instrctions
   # for how to save data when next button clicked
   def saveData(self, person):
      return
      #person.height = self.BMIresultText.get(1.0, tk.END)
      #print("saved " + person.height + " to person.height")

   # example function called when frame is rendered onto the screen
   # to load up data incase user has already entered data for person
   def loadData(self, person):
      return
      #print("loading data for BMI frame")
      #print("height: " + person.height)
      #if person.height != "":
        #print("inserting text " + person.height)    
        #self.BMIresultText.delete(1.0, tk.END)
        #self.BMIresultText.insert(END, person.height)
