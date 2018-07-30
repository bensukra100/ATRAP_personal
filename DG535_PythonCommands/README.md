# Programming DG535 with Python using the PYVISA module

This repository includes list of typical commands for the DG535 pulse generator in Python with explanations on how to use them. A full list of commands can be found in the [manual](https://www.thinksrs.com/downloads/pdfs/manuals/DG535m.pdf). Some example scripts that can be run are also given in this repository.  

## Getting Started

The DG535 can be communicated with using a GPIB cable and the examples shown in this repository assume this interface.

### Prerequisites

The commands require the use of the PYVISA module which can be installed from the terminal in the typical way:

```
pip install pyvisa
```

## Example Commands

These commands can be run from the terminal/command line. There are two command types: 'write'and 'inquiry', and it becomes obvious which ones to use where. However, first the instrument must be set up:


```
import pyvisa as visa

## listing available resources connected to the computer
rm = visa.ResourceManager()
print(rm.list_resources())
```

Once the instrument is located, it can be assigned as an variable in the script. In the examples shown in this repository, the DG535 exists on the channel: 'GPIB0::15::INSTR'

```
#Setting instrument DG535 to variable DG535
DG535 = rm.open_resource('GPIB0::15::INSTR') 
```

Writing commands to the instrument look like this:

```
#CLEAR INSTRUMENT 
DG535.write('CL')
```

And inquiring the state of the instrument can be done like this:

```
#CLEAR INSTRUMENT 
DG535.write('CL')
```

## Built With

* [PyVISA](https://pyvisa.readthedocs.io/en/stable/) - package used to communicate with the instrument


## Authors

* **Benedict Sukra** - [bensukra100](https://github.com/bensukra100)
* **Daniel Zambrano** - [dmartine](https://gitlab.cern.ch/dmartine)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
