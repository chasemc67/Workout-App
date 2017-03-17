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
#from frames.DataEntry import DataEntry
from frames.ScrollingResults import ScrollingResults

from frames.Entry import Entry

from Person import Person

from Database.DB import *
#from pdf.generatePdf import *

import os as os
import sys, subprocess

TITLE_FONT = ("Helvetica", 18, "bold")

createDB()
#insertTestPeople()
#testDBStuff()
#exit()

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
       self.container = container

       #self.framesToCycle = list()
       self.currentFrameIndex = 0

       self.person = Person()

       self.frames = {}
       for F in (Entry, MainPage, Circumference, ThreeSiteSkinfold, SvnSiteSkinfold, ModAst, Ebelling, Rockport, Coopers, MBtoss, VertJump, RMtest, RMpredict, GripStrength, PushUps, CurlUps, PlankEnd, WallSit, FlexTests, SLstance, DeepSquat, WallSlide, HipHinge, FrontPlank):
           page_name = F.__name__
           frame = F(parent=container, controller=self)
           self.frames[page_name] = frame

           # put all of the pages in the same location;
           # the one on the top of the stacking order
           # will be the one that is visible.
           frame.grid(row=0, column=0, sticky="nsew")

       self.show_frame("Entry")

   def save_person(self, alertObject):
      try:
      #if getattr(self.controller.person, "dbID") != "":
        dbID = getattr(self.person, "dbID")
        updatePerson(self.person)
        alertObject["text"] = "Updated person successfully"
        return
        # update entry instead of adding new person     
      except:
      #else:
        insertPerson(self.person)
        alertObject["text"] = "Saved person successfully"

   def print_person(self):
      #generatePdfForPerson(self.person)
      if sys.platform == "darwin":
        subprocess.call(['open', 'form.pdf'])
      else:
        os.startfile('form.pdf', 'open')



   def show_frame(self, page_name):
       '''Show a frame for the given page name'''
       self.currentFrameIndex = 0
       frame = self.frames[page_name]
       frame.tkraise()
       # TODO refactor out into one function
       try:
        frame.loadData(self.person)
        print("loaded data successfully")
       except AttributeError as e:
        print("frame has no loadData function")
        print(e)

   def start_main(self):
       '''Show a frame for the given page name'''
       self.currentFrameIndex = 0
       frame = MainPage(parent=self.container, controller=self)
       frame.grid(row=0, column=0, sticky="nsew")
       frame.tkraise()
       # TODO refactor out into one function
       try:
        frame.loadData(self.person)
        print("loaded data successfully")
       except AttributeError as e:
        print("frame has no loadData function")
        print(e)


   def next_page(self, saveFunction=None):
       if saveFunction:
        saveFunction(self.person)

       # Testing aggregate data entry stuff
       #frame = self.frames["DataEntry"]
       #frame.tkraise()
       #return

       # to get the results page to show as the last frame, you can
       # do something like:
       # if !self.frames[self.famesToCycle[self.currentFrameIndex]]:
       # frame = self.frames["resultsFrame"]
       #else:
       # Keep in mind the above code wont just work out of the box, 
       # You'll need to modify and play with it a little bit

       if (self.currentFrameIndex < len(self.person.framesChecked)) and (self.person.framesChecked[self.currentFrameIndex] == "BMIframe"):
        self.currentFrameIndex += 1

       if (self.currentFrameIndex == len(self.person.framesChecked)):
        #frame = self.frames["Results"]
        #frame = self.frames["ScrollingResults"]
        frame = ScrollingResults(parent=self.container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
       else:
        frame = self.frames[self.person.framesChecked[self.currentFrameIndex]]
        self.currentFrameIndex += 1
       frame.tkraise()
       # TODO refactor out into one function
       try:
        frame.loadData(self.person)
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
       # We specify attribute error because we want to skip
       # If frame doesn'r specify a load function, but we 
       # Want to be notified, if the load funciton fails for
       # some other reason
       except AttributeError:  
        print("frame has no loadData function")

   def getPerson(self):
    return self.person

def main():
  app = WorkoutApp()
  app.mainloop() 

main()
   

