"""
    FigureInterface - A class representing a figure for plotting.

    Examples:
    >>> figure_data = {
    ...     "title": "Plot Title",
    ...     "legend_position": "upper right",
    ...     "lines": [
    ...         {"color": "blue", "style": "--", "legend": "Line 1", "marker": "o", "xdata": [1, 2, 3], "ydata": [4, 5, 6]},
    ...         {"color": "red", "style": "-", "legend": "Line 2", "marker": "x", "xdata": [1, 2, 3], "ydata": [7, 8, 9]}
    ...     ]
    ... }
    >>> figure_instance = FigureInterface(figure_data)

    # Access figure properties
    >>> figure_instance.title
    'Plot Title'
    >>> figure_instance.legendPosition
    'upper right'
    >>> len(figure_instance.lines)
    2
    >>> figure_instance.lines[0].data
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> figure_instance.lines[1].kwargs
    {'color': 'red', 'linestyle': '-', 'label': 'Line 2', 'marker': 'x'}
    
    Author:
    CASALE Benjamin 

    Date:
    02/01/2024
    """

from typing import Dict,List,Union
import pandas
import numpy
from dataclasses import dataclass
from .linesInterface import LineInterface
from .utils import check_in_dict

@dataclass
class FigureLegend:
    text:List[str]
    position:str

class FigureInterface:
    """
    FigureInterface - A class representing a figure for plotting.

    Attributes:
    - _data (Dict): The raw data dictionary containing information about the figure.
    - _lines (List[LineInterface]): List of LineInterface instances representing lines to be plotted.
    - _title (str): The title of the figure. Defaults to an empty string if not specified.
    - _legend (str): The legend position for the figure. Defaults to None if not specified.

    Properties:
    - lines (List[LineInterface]): Read-only property returning the list of lines in the figure.
    - title (str): Read-only property returning the title of the figure.
    - legendPosition (str): Read-only property returning the legend position for the figure.

    Methods:
    - __init__(self, data: Dict) -> None:
        Initialize a FigureInterface instance with the provided data.

    """

    def __init__(self, data: Dict) -> None:
        """
        Initialize a FigureInterface instance with the provided data.

        Parameters:
        - data (Dict): A dictionary containing information about the figure.
        """
        self._data = data
        self.xlabel, self.ylabel, self.zlabel = self._getLabels()
        self._legend = check_in_dict(data, "legend_position", None)
        self._title = check_in_dict(data, "title", "")
        self._lines = self._getLines()

    @property
    def lines(self) -> List[LineInterface]:
        """Read-only property returning the list of lines in the figure."""
        return self._lines

    @property
    def title(self) -> str:
        """Read-only property returning the title of the figure."""
        return self._title

    @property
    def legendPosition(self) -> str:
        """Read-only property returning the legend position for the figure."""
        return self._legend

    def _getLines(self) -> List[LineInterface]:
        """
        Extract and return a list of LineInterface instances representing lines to be plotted.

        Returns:
        List[LineInterface]: List of LineInterface instances.
        """
        lines = []
        if "lines" in self._data:
            for line in self._data["lines"]:
                lines.append(LineInterface(line))

        if not lines:
            raise Exception("There must be at least one line to plot in the figure")
        return lines

    def _getLabels(self):
        """
        Extract and return axis labels for the figure.

        Returns:
        Tuple[str, str, str]: The x, y, and z-axis labels.
        """
        xlabel = check_in_dict(self._data, "xlabel", "")
        ylabel = check_in_dict(self._data, "ylabel", "")
        second = check_in_dict(self._data, "second_axe", False)
        if second == "true":
            second = True
            zlabel = check_in_dict(self._data, "zlabel", "")
        else:
            zlabel = None
        return xlabel, ylabel, zlabel