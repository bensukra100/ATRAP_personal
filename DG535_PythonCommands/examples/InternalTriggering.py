####Internal Triggering of DG535 when run####
#This example script does the following:
#i) Sets up the instrument
#ii) Sets the trigger mode to internal trigger and sets delays for A,B,C,D
#iii) continuosly triggers at set frequency when run

#modules
rm = visa.ResourceManager()
print(rm.list_resources())

#CLEAR INSTRUMENT
DG535.write('CL')

#Setting Trigger Mode
DG535.write('TM 0')

#Setting Trigger Rate
#format is: 'TR mode, rate (Hz)'
DG535.write('TR 0, 150.54')

#setting delays from t0
#format is: 'DT target, relative to, delay (s)'
DG535.write('DT 2,1,0E-9') #A
DG535.write('DT 3,1,5E0') #B
DG535.write('DT 5,1,1E-3') #C
DG535.write('DT 6,5,1E-3') #D
