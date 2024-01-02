"""
LineInterface - A class representing a line for plotting.

Example Usage:
```python
line_data = {"color": "blue", "style": "--", "legend": "Line 1", "marker": "o", "xdata": [1, 2, 3], "ydata": [4, 5, 6]}
line_instance = LineInterface(line_data)

# Access line properties
print("Line data:", line_instance.data)
print("Line properties:", line_instance.kwargs)
"""

from typing import Dict
from numpy import array, ndarray
from .utils import check_in_dict  

class LineInterface:
    """
    LineInterface - A class representing a line for plotting.

    Attributes:
    - _data (Dict): The raw data dictionary containing information about the line.
    - _color (str): The color of the line. Defaults to None if not specified.
    - _style (str): The line style. Defaults to None if not specified.
    - _label (str): The legend label for the line. Defaults to None if not specified.
    - _marker (str): The marker style for data points on the line. Defaults to None if not specified.
    - _xdata (ndarray): The x-axis data for the line. Defaults to None if not specified.
    - _ydata (ndarray): The y-axis data for the line. Must be provided, otherwise, an exception is raised.

    Properties:
    - data (ndarray): Read-only property returning the combined x and y data as a 2D array.
    - kwargs (Dict): Read-only property returning a dictionary with line properties suitable for Matplotlib.

    Methods:
    - __init__(self, data: Dict) -> None:
        Initialize a LineInterface instance with the provided data.

    Example Usage:
    ```python
    line_data = {"color": "blue", "style": "--", "legend": "Line 1", "marker": "o", "xdata": [1, 2, 3], "ydata": [4, 5, 6]}
    line_instance = LineInterface(line_data)

    # Access line properties
    print("Line data:", line_instance.data)
    print("Line properties:", line_instance.kwargs)
    ```
    """

    def __init__(self, data: Dict) -> None:
        """
        Initialize a LineInterface instance with the provided data.

        Parameters:
        - data (Dict): A dictionary containing information about the line.
        """
        self._data = data
        self._color = check_in_dict(data, "color", None)
        self._style = check_in_dict(data, "style", None)
        self._label = check_in_dict(data, "legend", None)
        self._marker = check_in_dict(data, "marker", None)
        self._xdata = array(check_in_dict(data, "xdata", None))

        if "ydata" in data:
            self._ydata = array(data["ydata"])
        else:
            raise Exception("Line must have Y data")

    @property
    def data(self) -> ndarray:
        """Read-only property returning the combined x and y data as a 2D array."""
        return array([self._xdata, self._ydata])

    @property
    def kwargs(self) -> Dict:
        """Read-only property returning a dictionary with line properties suitable for Matplotlib."""
        return {
            "color": self._color,
            "linestyle": self._style,
            "label": self._label,
            "marker": self._marker
        }
