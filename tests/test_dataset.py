import pytest
import numpy as np
from plotish.dataset import DataSet, check_in_dict,FigureInterface

def test_dataset_creation():
    # Test creating DataSet instance
    description = "Test dataset"
    date = "2022-01-01"
    name = "Test"
    
    # Updated test data with valid lines
    line_data = {
        "color": "blue",
        "style": "-",
        "legend": "Test Line",
        "marker": "o",
        "xdata": [1, 2, 3],
        "ydata": [4, 5, 6]
    }
    
    figure_data = {
        "title": "Test Figure",
        "lines": [line_data]
    }

    data = [FigureInterface(figure_data)]
    
    dataset_instance = DataSet()
    dataset_instance.load(description, date, name, data)

    # Assert properties are set correctly
    assert dataset_instance.description == description
    assert dataset_instance.date == date
    assert dataset_instance.name == name
    assert dataset_instance.data == data

def test_dataset_load_file(test_dataset_file):
    # Test loading data from JSON
    filename = "./tests/template.json"  # Replace with the actual path to your test JSON file
    dataset_instance = DataSet()
    dataset_instance.load_file(test_dataset_file)

    # Assert properties are set correctly after loading from JSON
    # assert isinstance(dataset_instance.date, str)
    assert isinstance(dataset_instance.description, str)
    assert isinstance(dataset_instance.name, str)
    # assert isinstance(dataset_instance.data, list)
    # assert all(isinstance(fig, FigureInterface) for fig in dataset_instance.data)

def test_dataset_load_file_nonexistent_file():
    # Test loading data from a nonexistent JSON file
    filename = "nonexistent_file.json"
    dataset_instance = DataSet()

    with pytest.raises(FileNotFoundError):
        dataset_instance.load_file(filename)

# def test_dataset_get_metadata():
#     # Test getting metadata from raw data
#     raw_data = {"date": "2022-01-01", "description": "Test metadata"}
#     dataset_instance = DataSet()
#     dataset_instance._raw_data = raw_data

#     date, description = dataset_instance.getMetaData()
#     assert date == raw_data["date"]
#     assert description == raw_data["description"]

# def test_dataset_get_data():
#     # Test getting data from raw data
#     raw_data = {"data": [{"title": "Test Figure", "lines": []}]}
#     dataset_instance = DataSet()
#     dataset_instance._raw_data = raw_data

#     data, n = dataset_instance.getData()

#     assert n == 1
#     assert isinstance(data, np.ndarray)
#     assert len(data) == 1
#     assert isinstance(data[0], FigureInterface)

