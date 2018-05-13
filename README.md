#### Graphical Python application for workout data entry

My good friend Megan Denholm is a personal trainer, and wanted to learn how to code.  
We built this together, piece by piece, so she could learn to code.  
  

##### Feautures:
* Graphical input built using tkinter
* Dynamic page creation for different types of workout data entry
* SQL database for data persistence
* Packages into a windows installer for deployment on windows computers
* Prints results to PDF for printing



##### Dependencies:
```
brew install makensis
pip install reportlab
pip install pynsist
```

##### Run:
```
Pythin main.py
```

##### Build the installer:
pynsist installer.cfg
