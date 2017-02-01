# a frame that will contain all the frames for data entry correspoinding
# to checked boxes. 

import tkinter as tk
from buttons.NextButton import NextButton
from buttons.QuitButton import QuitButton
from Person import Person

from frames.BMIframe import BMIframe
from frames.Circumference import Circumference
from frames.Coopers import Coopers
from frames.CurlUps import CurlUps
from frames.DeepSquat import DeepSquat
from frames.Ebelling import Ebelling
from frames.FlexTests import FlexTests
from frames.FrontPlank import FrontPlank
from frames.GripStrength import GripStrength
from frames.HipHinge import HipHinge
from frames.MainPage import MainPage
from frames.MBtoss import MBtoss
from frames.ModAst import ModAst
from frames.PlankEnd import PlankEnd
from frames.PushUps import PushUps
from frames.RMpredict import RMpredict
from frames.RMtest import RMtest
from frames.Rockport import Rockport
from frames.SLstance import SLstance
#from frames.StartPage import StartPage
from frames.SvnSiteSkinfold import SvnSiteSkinfold
from frames.ThreeSiteSkinfold import ThreeSiteSkinfold
from frames.VertJump import VertJump
from frames.WallSit import WallSit
from frames.WallSlide import WallSlide


from frames.ScrollWindow import ScrollWindow

class DataEntry(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		scrollView = ScrollWindow(self)
		scrollView.pack()

		bmiFrame = BMIframe(scrollView.interior, self.controller)
		bmiFrame.pack()

		spacer = tk.Label(scrollView.interior)
		spacer.pack()

		circFrame = Circumference(scrollView.interior, self.controller)
		circFrame.pack()

		spacer = tk.Label(scrollView.interior)
		spacer.pack()

		coopFrame = Coopers(scrollView.interior, self.controller)		
		coopFrame.pack()

		spacer = tk.Label(scrollView.interior)
		spacer.pack()

		curlUpsFrame = CurlUps(scrollView.interior, self.controller)
		curlUpsFrame.pack()

		spacer = tk.Label(scrollView.interior)
		spacer.pack()		