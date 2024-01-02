import json
import pytest
import tempfile
import os 
from plotish import DataSet
from plotish import FigureInterface

@pytest.fixture
def test_dataset_file():
    data = {
        "date": "05/02/2023",
        "name": "example",
        "description": "Example",
        "data": [{
            "xlabel": "label",
            "ylabel": "label",
            "title": "test",
            "legend_position": "right",
            "lines": [
                {
                    "xdata": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    "ydata": [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
                    "color": "purple",
                    "style": "-",
                    "marker": "",
                    "legend": "legend1"
                },
                {
                    "xdata": [0, 1, 2, 3, 4],
                    "ydata": [1, 2, 3, 4, 5],
                    "color": "red",
                    "style": "--",
                    "marker": "",
                    "legend": "legend2"
                }
            ]
        }]
    }

    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as temp_file:
        json.dump(data, temp_file)
        temp_file_path = temp_file.name

    yield temp_file_path  # Provide the temporary file path to the test

    # Clean up: Delete the temporary file after the test
    if temp_file_path:
        try:
            os.remove(temp_file_path)
        except FileNotFoundError:
            pass
