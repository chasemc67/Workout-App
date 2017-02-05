# New results window that contains a scroll view of 
# each corresponding results frame

# a frame that will contain all the frames for data entry correspoinding
# to checked boxes. 

import tkinter as tk
#from buttons.NextButton import NextButton
from buttons.QuitButton import QuitButton
from Person import Person

from Database.DB import insertPerson

from resultsFrames.BMIResultFrame import BMIResultFrame
from resultsFrames.CircumferenceResultFrame import CircumferenceResultFrame

from frames.ScrollWindow import ScrollWindow

class ScrollingResults(tk.Frame):

	def savePerson(self):
		try:
			dbID = getattr(self.controller.person, "dbID")
			return
			# update entry instead of adding new person     
		except:
			insertPerson(self.controller.person)

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# create the scroll view
		scrollView = ScrollWindow(self)
		scrollView.pack()

		if "BMIframe" in self.controller.person.framesChecked:
			bmiFrame = BMIResultFrame(scrollView.interior, self.controller)
			bmiFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "Circumferences" in self.controller.person.framesChecked:
			circFrame = CircumferenceResultFrame(scrollView.interior, self.controller)
			circFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		self.SaveButton = tk.Button(self)
		self.SaveButton['text'] = "Save"
		self.SaveButton['fg'] = "black"
		self.SaveButton['command'] = self.savePerson
		self.SaveButton.pack()

		self.QuitButton = QuitButton(self, self.controller)
		self.QuitButton.pack()
