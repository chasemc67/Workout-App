# New results window that contains a scroll view of 
# each corresponding results frame

# a frame that will contain all the frames for data entry correspoinding
# to checked boxes. 

import tkinter as tk
#from buttons.NextButton import NextButton
#from buttons.QuitButton import QuitButton
from Person import Person


from resultsFrames.BMIResultFrame import BMIResultFrame


from frames.ScrollWindow import ScrollWindow

class ScrollingResults(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# create the scroll view
		scrollView = ScrollWindow(self)
		scrollView.pack()

		bmiFrame = BMIResultFrame(scrollView.interior, self.controller)
		bmiFrame.pack()

		spacer = tk.Label(scrollView.interior)
		spacer.pack()