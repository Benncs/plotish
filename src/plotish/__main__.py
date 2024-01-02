#!/usr/bin/python3
"""
plotish - A Python module for reading JSON files and creating plots with Matplotlib.

This module provides functionality for reading data from a JSON file and generating plots
using the Matplotlib library. It includes a Plottish class for plot generation.

Module Components:
- plotish/__init__.py: Main module initializing the Plottish class for plot generation.
- plotish/dataset.py: Module defining the DataSet class for handling plot data.
- plotish/interfaces/figureinterface.py: Module containing the FigureInterface class for defining plot attributes.
- plotish/figtype.py: Module defining the FigType enumeration for different figure types.

Example Usage:
    python3 -m plotish dataset.json out 

Note:
    This module assumes the existence of the DataSet and FigureInterface classes

Dependencies:
    - Matplotlib
    - DataSet class (defined in dataset.py)
    - FigureInterface class (defined in interfaces/figureinterface.py)
    - FigType enumeration 

Author:
    CASALE Benjamin

Date:
    02/01/2024
"""

import sys
from typing import List
from .dataset import DataSet
from . import Plottish, FigType
from . import make_out_folder,treat_warnings


def _print_help():
    help_message = r"""
Usage: python -m plotish <filename> [outfolder]
Generate and save plots from a JSON file using Matplotlib.

Options:
  <filename>: Path to the JSON file.
  [outfolder]: Optional. Path to the output folder. Defaults to 'out'.
"""
    print(help_message)

def main(argc: int, argv: List[str]):
    """
    Main function, the entry point of the script.

    Parameters:
    - argc (int): The number of command-line arguments.
    - argv (List[str]): List of command-line arguments.

    Usage:
    - The main function expects at least one command-line argument, which is the filename.
    - An optional second argument can be provided for specifying the output folder.
      If not provided, the default output folder is 'out'.

    Example:
    - main(2,["__main__.py","json_file"]  # Uses default output folder 'out' # Uses specified output folder 'custom_outfolder'
    - main(3,["__main__.py","json_file","custom_outfolder"]  # Uses default output folder 'out' # Uses specified output folder 'custom_outfolder'

    Raises:
    - SystemExit: If the required command-line arguments are not provided or an error occurs during execution.
    """
    
    if len(argv) < 2 or "--help" in argv or "-h" in argv:
        _print_help()
        sys.exit(0)

    filename = argv[1]
    outfolder = argv[2] if len(argv) == 3 else "out"

    make_out_folder(outfolder)
    ds = DataSet()

    try:
        ds.load_file(filename)
        print(f"dataset: {ds.name} is loaded")
        pl = Plottish(outfolder, [FigType.PNG, FigType.SHOW], ds)
        warns = pl.plot()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    treat_warnings(warns)

if __name__== "__main__":
    main(len(sys.argv), sys.argv)
