# New results window that contains a scroll view of 
# each corresponding results frame

# a frame that will contain all the frames for data entry correspoinding
# to checked boxes. 

import tkinter as tk
from Person import Person

from Database.DB import insertPerson
from Database.DB import updatePerson

from resultsFrames.BMIResultFrame import BMIResultFrame
from resultsFrames.CircumferenceResultFrame import CircumferenceResultFrame
from resultsFrames.CoopersResultFrame import CoopersResultFrame
from resultsFrames.CurlUpsResultFrame import CurlUpsResultFrame
from resultsFrames.DeepSquatResultFrame import DeepSquatResultFrame
from resultsFrames.EbbelingResultFrame import EbbelingResultFrame
from resultsFrames.FlexResultFrame import FlexResultFrame
from resultsFrames.FrontPlankResultFrame import FrontPlankResultFrame
from resultsFrames.GripStrengthResultFrame import GripStrengthResultFrame
from resultsFrames.HipHingeResultFrame import HipHingeResultFrame
from resultsFrames.MBTossResultFrame import MBTossResultFrame
from resultsFrames.ModAstResultFrame import ModAstResultFrame
from resultsFrames.PlankEndResultFrame import PlankEndResultFrame
from resultsFrames.PushUpsResultFrame import PushUpsResultFrame
from resultsFrames.RMPredictResultFrame import RMPredictResultFrame
from resultsFrames.RMTestResultFrame import RMTestResultFrame
from resultsFrames.RockportResultFrame import RockportResultFrame
from resultsFrames.SLStanceResultFrame import SLStanceResultFrame
from resultsFrames.SvnSiteResultFrame import SvnSiteResultFrame
from resultsFrames.ThreeSiteResultFrame import ThreeSiteResultFrame
from resultsFrames.VertJumpResultFrame import VertJumpResultFrame
from resultsFrames.WallSitResultFrame import WallSitResultFrame
from resultsFrames.WallSlideResultFrame import WallSlideResultFrame

from customWidgets.ScrollWindow import ScrollWindow
from customWidgets.QuitButton import QuitButton

class ScrollingResults(tk.Frame):

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

		if "Circumference" in self.controller.person.framesChecked:
			circFrame = CircumferenceResultFrame(scrollView.interior, self.controller)
			circFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "Coopers" in self.controller.person.framesChecked:
			coopersFrame = CoopersResultFrame(scrollView.interior, self.controller)
			coopersFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "CurlUps" in self.controller.person.framesChecked:
			curlUpsFrame = CurlUpsResultFrame(scrollView.interior, self.controller)
			curlUpsFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "DeepSquat" in self.controller.person.framesChecked:
			deepSquatFrame = DeepSquatResultFrame(scrollView.interior, self.controller)
			deepSquatFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "Ebelling" in self.controller.person.framesChecked:
			ebbelingFrame = EbbelingResultFrame(scrollView.interior, self.controller)
			ebbelingFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "FlexTests" in self.controller.person.framesChecked:
			flexFrame = FlexResultFrame(scrollView.interior, self.controller)
			flexFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "FrontPlank" in self.controller.person.framesChecked:
			frontPlankFrame = FrontPlankResultFrame(scrollView.interior, self.controller)
			frontPlankFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "GripStrength" in self.controller.person.framesChecked:
			gripStrengthFrame = GripStrengthResultFrame(scrollView.interior, self.controller)
			gripStrengthFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "HipHinge" in self.controller.person.framesChecked:
			hipHingeFrame = HipHingeResultFrame(scrollView.interior, self.controller)
			hipHingeFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "MBtoss" in self.controller.person.framesChecked:
			MBTossFrame = MBTossResultFrame(scrollView.interior, self.controller)
			MBTossFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "ModAst" in self.controller.person.framesChecked:
			ModAstFrame = ModAstResultFrame(scrollView.interior, self.controller)
			ModAstFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "PlankEnd" in self.controller.person.framesChecked:
			PlankEndFrame = PlankEndResultFrame(scrollView.interior, self.controller)
			PlankEndFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "PushUps" in self.controller.person.framesChecked:
			pushUpsFrame = PushUpsResultFrame(scrollView.interior, self.controller)
			pushUpsFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "RMpredict" in self.controller.person.framesChecked:
			RMpredictFrame = RMPredictResultFrame(scrollView.interior, self.controller)
			RMpredictFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "RMtest" in self.controller.person.framesChecked:
			RMtestFrame = RMTestResultFrame(scrollView.interior, self.controller)
			RMtestFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "Rockport" in self.controller.person.framesChecked:
			rockportFrame = RockportResultFrame(scrollView.interior, self.controller)
			rockportFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "SLstance" in self.controller.person.framesChecked:
			SLstanceFrame = SLStanceResultFrame(scrollView.interior, self.controller)
			SLstanceFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "SvnSiteSkinfold" in self.controller.person.framesChecked:
			SvnSiteFrame = SvnSiteResultFrame(scrollView.interior, self.controller)
			SvnSiteFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "ThreeSiteSkinfold" in self.controller.person.framesChecked:
			ThreeSiteFrame = ThreeSiteResultFrame(scrollView.interior, self.controller)
			ThreeSiteFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "VertJump" in self.controller.person.framesChecked:
			VertJumpFrame = VertJumpResultFrame(scrollView.interior, self.controller)
			VertJumpFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "WallSit" in self.controller.person.framesChecked:
			WallSitFrame = WallSitResultFrame(scrollView.interior, self.controller)
			WallSitFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		if "WallSlide" in self.controller.person.framesChecked:
			WallSlideFrame = WallSlideResultFrame(scrollView.interior, self.controller)
			WallSlideFrame.pack()
			spacer = tk.Label(scrollView.interior)
			spacer.pack()

		spacer = tk.Label(self)

		spacer.pack()
		self.saveAlert = tk.Label(self)
		self.saveAlert['text'] = ""
		self.saveAlert.pack()
		spacer.pack()

		self.buttonFrame = tk.Frame(self)
		self.buttonFrame.pack()

		self.SaveButton = tk.Button(self.buttonFrame)
		self.SaveButton['text'] = "Save"
		self.SaveButton['fg'] = "black"
		self.SaveButton['command'] = lambda: self.controller.save_person(self.saveAlert)
		self.SaveButton.grid(row=1, column=0)

		self.PrintButton = tk.Button(self.buttonFrame)
		self.PrintButton['text'] = "Print"
		self.PrintButton['fg'] = "black"
		self.PrintButton['command'] = self.controller.print_person
		self.PrintButton.grid(row=1, column=1)

		self.QuitButton = QuitButton(self.buttonFrame, self.controller)
		self.QuitButton.grid(row=1, column=2)
