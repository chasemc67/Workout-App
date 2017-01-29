#http://stackoverflow.com/questions/15672552/python-tkinter-listbox-get-active-method

import tkinter as tk
from buttons.NextButton import NextButton
from buttons.QuitButton import QuitButton

import Database.DB as DB

class Entry(tk.Frame):

   def select(self, event):
      self.controller.person = self.people[self.listbox.curselection()[0]]

   def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      self.controller = controller

      self.listbox = tk.Listbox(self)
      self.listbox.bind('<<ListboxSelect>>', self.select)

      self.people = DB.getPeople()

      for person in self.people:
            self.listbox.insert(tk.END, person.name)

      self.listbox.grid(row=0, column=0)
      #self.listbox.pack(fill=BOTH, expand=1)

      self.NewPerson = tk.Button(self)
      self.NewPerson['text'] = "New Person"
      self.NewPerson['fg'] = 'black'
      self.NewPerson['command'] = lambda: controller.show_frame("MainPage")
      self.NewPerson.grid(row=1, column=0)

      self.EditPerson = tk.Button(self)
      self.EditPerson['text'] = "Edit Selected"
      self.EditPerson['fg'] = 'black'
      self.EditPerson['command'] = lambda: controller.show_frame("MainPage")
      self.EditPerson.grid(row=1, column=1)

      


