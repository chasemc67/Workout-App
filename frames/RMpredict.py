import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class RMpredict(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.RMPredict = tk.Label(self)
       self.RMPredict["text"] = "1 Rep Max.(Predicted)"
       self.RMPredict.grid(row=0, column=0)

       self.RMPredictEx = tk.Label(self)
       self.RMPredictEx["text"] = "Exercise: "
       self.RMPredictEx.grid(row=1, column=0)

       self.RMPredictExText = tk.Text(self)
       self.RMPredictExText["height"] = 1
       self.RMPredictExText["width"] = 5
       self.RMPredictExText.grid(row=1, column=1)

       self.RMPredictReps = tk.Label(self)
       self.RMPredictReps["text"] = "Reps: "
       self.RMPredictReps.grid(row=2, column=0)

       self.RMPredictRepsText = tk.Text(self)
       self.RMPredictRepsText["height"] = 1
       self.RMPredictRepsText["width"] = 5
       self.RMPredictRepsText.grid(row=2, column=1)

       self.RMPredictLoad = tk.Label(self)
       self.RMPredictLoad["text"] = "Rep Weight(kg): "
       self.RMPredictLoad.grid(row=3, column=0)

       self.RMPredictLoadText = tk.Text(self)
       self.RMPredictLoadText["height"] = 1
       self.RMPredictLoadText["width"] = 5
       self.RMPredictLoadText.grid(row=3, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=4, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=4, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=4, column=2)

   def loadData(self, person):

       self.RMPredictExText.delete(1.0, tk.END)
       self.RMPredictExText.insert(tk.END, person.RMPredictEx)

       self.RMPredictRepsText.delete(1.0, tk.END)
       self.RMPredictRepsText.insert(tk.END, person.RMPredictReps)

       self.RMPredictLoadText.delete(1.0, tk.END)
       self.RMPredictLoadText.insert(tk.END, personRMPredictLoad)

   def saveData(self, person):
       person.RMPredictEx = self.RMPredictExText.get(1.0, tk.END)
       person.RMPredictReps = self.RMPredictRepsText.get(1.0, tk.END)
       person.RMPredictLoad = self.RMPredictLoadText.get(1.0, tk.END)
