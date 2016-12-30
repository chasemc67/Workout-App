import tkinter as tk

class MBtoss(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SeatMB = tk.Label(self)
       self.SeatMB["text"] = "Seated Med. Ball Toss"
       self.SeatMB.grid(row=0, column=0)

       self.SeatMBDist = tk.Label(self)
       self.SeatMBDist["text"] = "Max. Distance(cm): "
       self.SeatMBDist.grid(row=1, column=0)

       self.SeatMBDist = tk.Text(self)
       self.SeatMBDist["height"] = 1
       self.SeatMBDist["width"] = 5
       self.SeatMBDist.grid(row=1, column=1)

       self.NextE = tk.Button(self)
       self.NextE["text"] = "Next"
       self.NextE["fg"] = "black"
       self.NextE["command"] = lambda: controller.next_page()
       self.NextE.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitE = tk.Button(self)
       self.QuitE["text"] = "Quit"
       self.QuitE["fg"] = "black"
       self.QuitE["command"] = lambda: controller.show_frame("MainPage")
       self.QuitE.grid(row=2, column=2)