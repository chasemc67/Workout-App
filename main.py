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
from frames.Results import Results

from Person import Person

TITLE_FONT = ("Helvetica", 18, "bold")

#framesToCycle = list()
#currentFrameIndex = list()
#currentFrameIndex.append(0)

class WorkoutApp(tk.Tk):

   def __init__(self, *args, **kwargs):
       tk.Tk.__init__(self, *args, **kwargs)
       # the container is where we'll stack a bunch of frames
       # on top of each other, then the one we want visible
       # will be raised above the others
       container = tk.Frame(self)
       container.pack(side="top", fill="both", expand=True)
       container.grid_rowconfigure(0, weight=1)
       container.grid_columnconfigure(0, weight=1)

       #self.framesToCycle = list()
       self.currentFrameIndex = 0

       self.person = Person()

       self.frames = {}
       for F in (MainPage, Circumference, ThreeSiteSkinfold, SvnSiteSkinfold, ModAst, Ebelling, Rockport, Coopers, MBtoss, VertJump, RMtest, RMpredict, GripStrength, PushUps, CurlUps, PlankEnd, WallSit, FlexTests, SLstance, DeepSquat, WallSlide, HipHinge, FrontPlank, Results):
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
       # TODO refactor out into one function
       try:
        frame.loadData(self.person)
        print("loaded data successfully")
       except AttributeError:
        print("frame has no loadData function")

   def next_page(self, saveFunction=None):
       if saveFunction:
        saveFunction(self.person)

       # to get the results page to show as the last frame, you can
       # do something like:
       # if !self.frames[self.famesToCycle[self.currentFrameIndex]]:
       # frame = self.frames["resultsFrame"]
       #else:
       # Keep in mind the above code wont just work out of the box, 
       # You'll need to modify and play with it a little bit
       if (self.currentFrameIndex == len(self.person.framesChecked)):
        frame = self.frames["Results"]
       else:
        frame = self.frames[self.person.framesChecked[self.currentFrameIndex]]
       print(self.person.armCirc)
       self.currentFrameIndex += 1
       frame.tkraise()
       # TODO refactor out into one function
       try:
        frame.loadData(self.person)
        print("loaded data successfully")
       # We specify attribute error because we want to skip
       # If frame doesn'r specify a load function, but we 
       # Want to be notified, if the load funciton fails for
       # some other reason
       except AttributeError as e:
        print("Something went wrong loading data for frame")
        print(e)


   def prev_page(self):
       frame = self.frames[self.person.framesChecked[self.currentFrameIndex-1]]
       self.currentFrameIndex -= 1
       frame.tkraise()
       # TODO refactor out into one function
       try:
        frame.loadData(self.person)
        print("loaded data successfully")
       # We specify attribute error because we want to skip
       # If frame doesn'r specify a load function, but we 
       # Want to be notified, if the load funciton fails for
       # some other reason
       except AttributeError:  
        print("frame has no loadData function")

   def getPerson(self):
    return self.person

if __name__ == "__main__":
   app = WorkoutApp()
   app.mainloop()

