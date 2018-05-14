#### Graphical Python application for workout data entry

My good friend Megan Denholm is a personal trainer, and wanted to learn how to code.  
We built this together, piece by piece, so she could learn to code.  
  
 
<img width="733" alt="screen shot 2018-05-13 at 2 04 42 pm" src="https://user-images.githubusercontent.com/6922982/39971846-014dadce-56b8-11e8-9d8c-b999e32634ca.png">
<img width="1336" alt="screen shot 2018-05-13 at 2 16 09 pm" src="https://user-images.githubusercontent.com/6922982/39971858-47319616-56b8-11e8-8fe4-832f5706fe59.png">


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
```
pynsist installer.cfg
```
 
