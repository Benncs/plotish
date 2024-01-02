"""
plotish.dataset - Module for handling datasets and reading data for plotting.

This module defines the DataSet class, which is responsible for handling datasets used for plotting.
It provides methods for loading metadata and plot data, particularly from JSON files.

Classes:
- DataSet: A class representing a dataset with metadata and plot data.

Example Usage:
```python
from plotish.dataset import DataSet

# Create a DataSet instance
data_set = DataSet()

# Load data from a JSON file
data_set.load_json("path/to/your/data.json")

# Access metadata and plot data
print("Date:", data_set.date)
print("Description:", data_set.description)
print("Name:", data_set.name)
print("Number of plots:", len(data_set.data))

Author:
CASALE Benjamin

Date:
02/01/2024
"""

import pandas 
from typing import Tuple,List
import numpy 
from .interfaces.figureinterface import FigureInterface
from .interfaces.utils import check_in_dict
import datetime

class DataSet:
    """
    A class representing a dataset for plotting.

    Attributes:
    - _date (str): The date associated with the dataset.
    - _description (str): The description of the dataset.
    - _data (List[FigureInterface]): List of FigureInterface instances representing plot data.
    - _name (str): The name associated with the dataset.

    Methods:
    - load(description: str, date: str, name: str, data: List[FigureInterface]) -> None:
        Load the dataset with provided metadata and data.

    - load_json(filename: str) -> None:
        Load the dataset from a JSON file.

    - getMetaData() -> Tuple[str, str]:
        Extract and return metadata (date and description) from the raw data.

    - getData() -> Tuple[numpy.ndarray, int]:
        Extract and return plot data from the raw data.

    - _openfile(filename: str) -> pandas.DataFrame:
        Open and read a JSON file into a pandas DataFrame.

    Properties:
    - date (str): Read-only property returning the dataset's date.
    - description (str): Read-only property returning the dataset's description.
    - data (List[FigureInterface]): Read-only property returning the dataset's plot data.
    - name (str): Read-only property returning the dataset's name.
    """

    @property
    def date(self) -> str:
        """Read-only property returning the dataset's date."""
        return self._date

    @property
    def description(self) -> str:
        """Read-only property returning the dataset's description."""
        return self._description

    @property
    def data(self) -> List[FigureInterface]:
        """Read-only property returning the dataset's plot data."""
        return self._data

    @property
    def name(self) -> str:
        """Read-only property returning the dataset's name."""
        return self._name

    def __init__(self) -> None:
        """
        Initialize an empty DataSet.
        """
        pass

    def load(self, description: str, date: str, name: str, data: List[FigureInterface]) -> None:
        """
        Load the dataset with provided metadata and data.

        Parameters:
        - description (str): The description of the dataset.
        - date (str): The date associated with the dataset.
        - name (str): The name associated with the dataset.
        - data (List[FigureInterface]): List of FigureInterface instances representing plot data.
        """
        self._date = date
        self._name = name
        self._description = description
        self._data = data

    def load_file(self, filename: str) -> None:
        """
        Load the dataset from a file.

        Parameters:
        - filename (str): The path to the JSON file.
        """
        self._raw_data = DataSet._openfile(filename)
        self._date, self._description = self._getMetaData()
        self._data, self._n = self._getData()
        self._name = check_in_dict(self._raw_data, "name", "figure")[0]

    def _getMetaData(self) -> Tuple[str, str]:
        """
        Extract and return metadata (date and description) from the raw data.

        Returns:
        Tuple[str, str]: The date and description associated with the dataset.
        """
        date = check_in_dict(self._raw_data, "date", ["01/01/1900"])[0]
        description = check_in_dict(self._raw_data, "description", ["No description"])[0]
        return date, description

    def _getData(self) -> Tuple[numpy.ndarray, int]:
        """
        Extract and return plot data from the raw data.

        Returns:
        Tuple[numpy.ndarray, int]: The plot data and the number of plots in the dataset.
        """
        if "data" in self._raw_data:
            n = len(self._raw_data["data"])
            data = []
            for i, fig in enumerate(self._raw_data["data"]):
                data.append(FigureInterface(fig))
        else:
            n = 0
            data = numpy.empty((0))
        return numpy.array(data), n

    @staticmethod
    def _openfile(filename: str) -> pandas.DataFrame:
        """
        Open and read a JSON file into a pandas DataFrame.

        Parameters:
        - filename (str): The path to the JSON file.

        Returns:
        pandas.DataFrame: The content of the JSON file as a pandas DataFrame.
        """
        return pandas.read_json(filename)
