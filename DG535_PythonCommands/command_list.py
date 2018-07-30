####List of Commands that can be passed to DG535####
# this script is not intended to be run
# it is merely for reference of the Commands

##importing the pyVISA module
import pyvisa as visa

##listing available resources
rm = visa.ResourceManager()
print(rm.list_resources())

##setting up the instrument
DG535 = rm.open_resource('GPIB0::15::INSTR')

#CLEAR INSTRUMENT
DG535.write('CL')

##CHECK FOR ERRORS
DG535.inquery('ES')

##TRIGGER COMMANDS
#Trigger Modes
DG535.write('TM 0') #0,1,2,3 means Int, Ext, SS, Burst

#Trigger Level
DG535.write('TL 1') #volts

##DELAYS
##CHANNELS: 0,1,2,3,4,5,6,7
##Trig In, T0 Out, A Out, B Out, AB and -AB Out
##C Out, D Out, CD and -CD Out
#DT i{,j,t}
#Delay Time of channel i is set to t seconds relative to
#channel j.
DG535.write('DT 3,2,1.2E-6')

##single shot command
DG535.write('SS')
