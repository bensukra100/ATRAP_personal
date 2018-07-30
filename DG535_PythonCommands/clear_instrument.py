####Script to run to clear instrument####

import pyvisa as visa

#Setting instrument DG535 to variable DG535
rm = visa.ResourceManager()
DG535 = rm.open_resource('GPIB0::15::INSTR')

#CLEAR INSTRUMENT
DG535.write('CL')
