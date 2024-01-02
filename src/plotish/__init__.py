"""
plottish - Module for creating and saving plots using Matplotlib.

This module defines a class, Plottish, that facilitates the creation and saving of plots.
It includes support for various figure types, such as PDF, PGF, PNG, SVG, and the option to
display the figure directly without saving it. The module also provides functionality for
handling warnings during the plotting process.

Usage:
    from plottish import Plottish, FigType, Dataset

    # Example usage:
    out_folder = "./output"
    figure_types = [FigType.PDF, FigType.PNG, FigType.SHOW]
    data_set = your_data_set_instance  # Replace with your actual DataSet instance

    plottish_instance = Plottish(out_folder, figure_types, data_set)
    warnings = plottish_instance.plot()

    # Process warnings or take further actions based on the generated plots.

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


import os

import matplotlib.pyplot as plt 
from enum import Enum
from typing import List ,Tuple

from .dataset import DataSet
from .interfaces.figureinterface import FigureInterface
from .interfaces.linesInterface import LineInterface
from importlib.metadata import version 
__version__ = version("plotish")


def make_out_folder(dir: str):
    """
    Create the specified folder and its parent directories if they don't exist.

    Parameters:
    - dir (str): The path of the folder to be created.

    Raises:
    - OSError: If an error occurs during folder creation (excluding 'File exists' errors).

    Comments:
    - This function uses os.makedirs with exist_ok=True to ensure that the folder and its parent directories
      are created if they don't exist. It suppresses 'File exists' errors.
    """
    try:
        os.makedirs(dir, exist_ok=True)
    except OSError as e:
        if e.errno != 17:  # Ignore 'File exists' errors
            print(e)

def treat_warnings(warnings: List[str]):
    """
    Print warning messages to the console, excluding messages with the value 'OK'.

    Parameters:
    - warnings (List[str]): List of warning messages to be processed.

    Comments:
    - This function iterates over the provided list of warnings and prints each message to the console.
      Warnings with the value 'OK' are excluded from printing.
    """
    for warn in warnings:
        if warn != "OK":
            print("Warning:", warn)




class FigType(Enum):
    """
    Enumeration representing different types of figures.

    Enumeration Values:
    - PDF (int): Value 0, representing the PDF file format.
    - PGF (int): Value 1, representing the PGF (Portable Graphics Format) file format.
    - PNG (int): Value 2, representing the PNG (Portable Network Graphics) file format.
    - SVG (int): Value 3, representing the SVG (Scalable Vector Graphics) file format.
    - SHOW (int): Value 4, representing the option to display the figure rather than saving it.

    Comments:
    - This enumeration defines symbolic names for different types of figure formats,
      making the code more readable and self-explanatory.
    - Each enumeration value is assigned a unique integer value for easy comparison and identification.
    - The 'SHOW' option allows displaying the figure directly instead of saving it to a file.
    """
    PDF=0,
    PGF=1,
    PNG=2,
    SVG=3,
    SHOW=4,
    

class Plottish:
    """
    Class for creating and saving plots.

    Attributes:
    - _outfolder (str): The output folder for saving plots.
    - _dataset (DataSet): The dataset containing plot data.
    - types (List[FigType]): List of figure types to generate.
    """

    def __init__(self, outfolder: str, types: List[FigType], dataset: DataSet) -> None:
        """
        Initialize a Plottish instance.

        Parameters:
        - outfolder (str): The output folder for saving plots.
        - types (List[FigType]): List of figure types to generate.
        - dataset (DataSet): The dataset containing plot data.
        """
        self._outfolder = outfolder
        self._dataset = dataset
        plt.style.use('ggplot')
        self.types = types
        self._show = False

    def plot(self) -> List[str]:
        """
        Create and save plots for each figure in the dataset.

        Returns:
        List[str]: List of warnings generated during the plot generation.
        """
        warns = []
        for i, fig in enumerate(self._dataset.data):
            fig, warn = self.make_fig(fig)
            for fig_type in self.types:
                self.save(fig_type, i)
            warns.append(warn)

        if self._show:
            plt.show()
        return warns

    def save(self, fig_type: FigType, i: int) -> None:
        """
        Save the current plot in a specified format.

        Parameters:
        - fig_type (FigType): The type of figure to save.
        - i (int): Index of the current figure in the dataset.
        """
        name = f"{self._outfolder}/{self._dataset.name}_{i}"
        match fig_type:
            case FigType.PDF:   
                plt.savefig(f"{name}.pdf",backend="pgf",dpi=300)
            case FigType.PGF:
                plt.savefig(f"{name}.pgf",backend="pgf",dpi=300)
            case FigType.PNG:
                plt.savefig(f"{name}.png",dpi=300)
            case FigType.SVG:
                plt.savefig(f"{name}.svg",dpi=300)
            case FigType.SHOW:
                # plt.show()
                self._show = True
            case _:
                plt.savefig(f"{name}.png",dpi=50)      

    def make_fig(self, fi: FigureInterface) -> Tuple[plt.Figure, str]:
        """
        Create a new figure and plot data from FigureInterface.

        Parameters:
        - fi (FigureInterface): An interface containing data for plotting.

        Returns:
        Tuple[plt.Figure, str]: The generated figure and a warning message.
        """
        fig, ax = plt.subplots()
        ax.set_title(fi.title)
        ax.set_xlabel(fi.xlabel)
        ax.set_ylabel(fi.ylabel)

        for line in fi.lines:
            ax.plot(line._xdata, line._ydata, **line.kwargs)

        try:
            if fi.legendPosition is not None and fi.legendPosition != "None":
                ax.legend(loc=fi.legendPosition)
        except Exception as e:
            ax.legend(loc="best")
            return fig, f"Plotting:makefig legend:\r\n{str(e)}"

        return fig, "OK"

