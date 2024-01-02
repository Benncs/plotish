import pytest
from plotish import Plottish, FigType,DataSet,FigureInterface


@pytest.fixture
def sample_dataset():
    # Create a sample DataSet instance for testing
    line_data_1 = {
        "xdata": [1, 2, 3],
        "ydata": [4, 5, 6],
        "color": "blue",
        "style": "-",
        "marker": "o",
        "legend": "Line 1"
    }

    line_data_2 = {
        "xdata": [1, 2, 3],
        "ydata": [7, 8, 9],
        "color": "red",
        "style": "--",
        "marker": "x",
        "legend": "Line 2"
    }

    figure_data_1 = {
        "title": "Test Figure 1",
        "lines": [line_data_1]
    }

    figure_data_2 = {
        "title": "Test Figure 2",
        "lines": [line_data_2]
    }

    data = [
        FigureInterface(figure_data_1),
        FigureInterface(figure_data_2)
    ]

    ds = DataSet()
    ds.load("Sample Dataset", "2022-01-01", "Test", data)
    return ds

def test_plottish_init():
    # Test the initialization of Plottish class
    outfolder = "./output"
    types = [FigType.PNG, FigType.SHOW]
    dataset = sample_dataset
    plottish_instance = Plottish(outfolder, types, dataset)

    assert plottish_instance._outfolder == outfolder
    assert plottish_instance.types == types
    assert plottish_instance._dataset == dataset

# def test_plottish_plot(sample_dataset, capsys):
#     # Test the plot method of Plottish class
#     outfolder = "./output"
#     types = [FigType.PNG, FigType.SHOW]
#     plottish_instance = Plottish(outfolder, types, sample_dataset)

#     # Suppress the actual plotting for testing
#     plottish_instance.makeFig = lambda x: (None, "OK")

#     # Capture console output
#     with capsys.disabled():
#         # Call the plot method
#         warnings = plottish_instance.plot()

#     # Capture the printed output
#     captured = capsys.readouterr()

#     # Check if the correct warnings are printed
#     assert "Warning: OK" in captured.out

#     # Check if the return value is as expected
#     assert warnings == ["OK"]

