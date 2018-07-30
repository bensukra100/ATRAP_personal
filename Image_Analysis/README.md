# Image Analysis Script

This script was written to analyse the image taken from the [Thorlabs CS2100-USB - Quantalux Camera](https://www.thorlabs.com/thorproduct.cfm?partnumber=CS2100M-USB) that was being used to image and characterise the antiproton plasma and the pulsed beam from the positron accumulator. The antiproton plasmas/ positron cloud are made to collide with an MCP+phosphor screen set-up and the resulting fluorescence from the phosphor screen is captured by the camera. 

The script first does a background subtraction using an image captured when the plasma is not incident then finds the center of the plasma incident on the MCP+phosphor screen apparatus by fitting a 2D gaussian to the image. The vertical and horizontal profiles through this center is then generated. These profiles give some indication of the plasma size and, in the case of the positron plasmas, gives an indication of compression by the rotating wall in the positron accumulator and if clipping of the beam occurs during transfer to the antiproton trap. 

This script only performs analysis from a saved image but can be easily incorporated with other scripts that have the functionality to directly capture an image. This script has been built to image positron and antiproton plasmas but can easily be used in other scenarious. 
  

## Getting Started

The script is written in Python and can be run from a Jupyter notebook or directly from the terminal. Both the Jupyter notebook and the .py file are included in this repository.

### Prerequisites

The script uses the `numpy`, `matplotlib`, `scipy`, `imageio`, `datetime` and `os` modules. These can be installed in the typical way but it's likely that these modules are already installed:

```
pip install imageio
```

## Authors

* **Benedict Sukra** - [bensukra100](https://github.com/bensukra100)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* **Alberto Alonso** - [Alberto-masm](https://github.com/Alberto-masm) This is script is similar to a script produced by Alberto for a similar system in the Positronium Spectroscopy Group at University College London. 
