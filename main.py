import tkinter as tk   # python3
#import Tkinter as tk   # python

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


TITLE_FONT = ("Helvetica", 18, "bold")

#framesToCycle = list()
#currentFrameIndex = list()
#currentFrameIndex.append(0)

class SampleApp(tk.Tk):

   def __init__(self, *args, **kwargs):
       tk.Tk.__init__(self, *args, **kwargs)
       # the container is where we'll stack a bunch of frames
       # on top of each other, then the one we want visible
       # will be raised above the others
       container = tk.Frame(self)
       container.pack(side="top", fill="both", expand=True)
       container.grid_rowconfigure(0, weight=1)
       container.grid_columnconfigure(0, weight=1)

       self.framesToCycle = list()
       self.currentFrameIndex = 0

       self.frames = {}
       for F in (MainPage, BMIframe, Circumference, ThreeSiteSkinfold, SvnSiteSkinfold, ModAst, Ebelling, Rockport, Coopers, MBtoss, VertJump, RMtest, RMpredict, GripStrength, PushUps, CurlUps, PlankEnd, WallSit, FlexTests, SLstance, DeepSquat, WallSlide, HipHinge, FrontPlank):
           page_name = F.__name__
           frame = F(parent=container, controller=self)
           self.frames[page_name] = frame

           # put all of the pages in the same location;
           # the one on the top of the stacking order
           # will be the one that is visible.
           frame.grid(row=0, column=0, sticky="nsew")

       self.show_frame("MainPage")


   def show_frame(self, page_name):
       '''Show a frame for the given page name'''
       self.currentFrameIndex = 0
       frame = self.frames[page_name]
       frame.tkraise()

   def next_page(self):
       frame = self.frames[self.framesToCycle[self.currentFrameIndex]]
       self.currentFrameIndex += 1
       frame.tkraise()

   def prev_page(self):
       frame = self.frames[self.framesToCycle[self.currentFrameIndex-1]]
       self.currentFrameIndex -= 1
       frame.tkraise()

if __name__ == "__main__":
   app = SampleApp()
   app.mainloop()

