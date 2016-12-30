import tkinter as tk

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

       self.RMPredictEx = tk.Text(self)
       self.RMPredictEx["height"] = 1
       self.RMPredictEx["width"] = 5
       self.RMPredictEx.grid(row=1, column=1)

       self.RMPredictReps = tk.Label(self)
       self.RMPredictReps["text"] = "Reps: "
       self.RMPredictReps.grid(row=2, column=0)

       self.RMPredictReps = tk.Text(self)
       self.RMPredictReps["height"] = 1
       self.RMPredictReps["width"] = 5
       self.RMPredictReps.grid(row=2, column=1)

       self.RMPredictEst = tk.Label(self)
       self.RMPredictEst["text"] = "Estimated 1RM(kg): "
       self.RMPredictEst.grid(row=3, column=0)

       self.RMPredictEst = tk.Text(self)
       self.RMPredictEst["height"] = 1
       self.RMPredictEst["width"] = 5
       self.RMPredictEst.grid(row=3, column=1)

       self.NextD = tk.Button(self)
       self.NextD["text"] = "Next"
       self.NextD["fg"] = "black"
       self.NextD["command"] = lambda: controller.next_page()
       self.NextD.grid(row=4, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=4, column=1)

       self.QuitD = tk.Button(self)
       self.QuitD["text"] = "Quit"
       self.QuitD["fg"] = "black"
       self.QuitD["command"] = lambda: controller.show_frame("MainPage")
       self.QuitD.grid(row=4, column=2)