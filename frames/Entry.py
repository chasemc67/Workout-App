#http://stackoverflow.com/questions/15672552/python-tkinter-listbox-get-active-method

# Entry page to the application
# This is the window with the DB view, and the New/Edit person buttons

import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton
from Person import Person

import Database.DB as DB

class Entry(tk.Frame):

   def select(self, event):
      self.controller.person = self.people[self.listbox.curselection()[0]]

   def createNewPerson(self):
      self.controller.person = Person()
      self.controller.show_frame("MainPage")

   def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      self.controller = controller

      self.titleLabel = tk.Label(self, font=("Courier", 30))
      self.titleLabel['text'] = "MacEwan University Sports and Wellness"
      self.titleLabel.pack()

      spacer = tk.Label(self)
      spacer.pack()
      spacer = tk.Label(self)
      spacer.pack()

      self.centerFrame = tk.Frame(self)

      self.listFrame = tk.Frame(self)
      self.scrollBar = tk.Scrollbar(self.listFrame, orient=tk.VERTICAL)
      self.listbox = tk.Listbox(self.listFrame, yscrollcommand=self.scrollBar.set)
      self.scrollBar.config(command=self.listbox.yview)
      self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
      self.listbox['width'] = 30
      self.listbox.bind('<<ListboxSelect>>', self.select)
      #self.listbox.grid(row=0, column=0)
      self.listbox.pack()
      #self.listbox.pack(fill=BOTH, expand=1)
      self.listFrame.pack()

      spacer = tk.Label(self)
      spacer.pack()
      spacer = tk.Label(self)
      spacer.pack()

      self.buttonFrame = tk.Frame(self)
      self.buttonFrame.pack()

      self.NewPerson = tk.Button(self.buttonFrame)
      self.NewPerson['text'] = "New Person"
      self.NewPerson['fg'] = 'black'
      self.NewPerson['command'] = self.createNewPerson
      self.NewPerson.grid(row=1, column=0)

      self.EditPerson = tk.Button(self.buttonFrame)
      self.EditPerson['text'] = "Edit Selected"
      self.EditPerson['fg'] = 'black'
      self.EditPerson['command'] = lambda: controller.start_main()
      self.EditPerson.grid(row=1, column=1)

      self.PrintPerson = tk.Button(self.buttonFrame)
      self.PrintPerson['text'] = "Print Selected"
      self.PrintPerson['fg'] = 'black'
      self.PrintPerson['command'] = lambda: controller.print_person()
      self.PrintPerson.grid(row=1, column=2)

      

   def loadData(self, person):
      self.people = DB.getPeople(50)
      self.people.sort(key=lambda x: x.dbID, reverse=True)

      self.listbox.delete(0, tk.END)

      for person in self.people:
            self.listbox.insert(tk.END, (person.testDate + "          " + person.name))
