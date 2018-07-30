####Trigger single shot on key pressed####
#This example script does the following:
#i) Sets up the instrument
#ii) Sets the trigger mode to single shot and sets delays for A,B,C,D
#iii) Triggers a single shot when space bar key is pressed

#modules
import win32api
import pyvisa as visa

#setting up instrument
rm = visa.ResourceManager()
DG535 = rm.open_resource('GPIB0::15::INSTR')

#CLEAR INSTRUMENT
DG535.write('CL')

#Setting Trigger Mode
DG535.write('TM 2')

#setting delays from t0
#the structure is as follows: 'DT target, relative to, delay (s)'
DG535.write('DT 2,1,0E-9') #A
DG535.write('DT 3,1,5E0') #B
DG535.write('DT 5,1,1E-3') #C
DG535.write('DT 6,5,1E-3') #D


## loop to wait on space bar pressed
initial_state = win32api.GetKeyState(0x20)
while True:
    current_state = win32api.GetKeyState(0x20)
    if current_state != initial_state:
        initial_state = current_state
        if  current_state < 0:
            DG535.write('SS') #command to run single shot
