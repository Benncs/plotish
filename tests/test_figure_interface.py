import pytest
from plotish import FigureInterface

def test_figure_interface_creation():
    # Test creating FigureInterface instance
    figure_data = {
        "title": "Test Title",
        "legend_position": "upper left",
        "lines": [
            {"color": "green", "style": "--", "legend": "Line A", "marker": "s", "xdata": [1, 2, 3], "ydata": [4, 5, 6]},
            {"color": "orange", "style": "-", "legend": "Line B", "marker": "o", "xdata": [1, 2, 3], "ydata": [7, 8, 9]}
        ]
    }
    figure_instance = FigureInterface(figure_data)

    # Assert properties are set correctly
    assert figure_instance.title == "Test Title"
    assert figure_instance.legendPosition == "upper left"
    assert len(figure_instance.lines) == 2

def test_figure_interface_no_lines():
    # Test creating FigureInterface instance with no lines (should raise an exception)
    figure_data = {
        "title": "No Lines Title",
        "legend_position": "lower right",
        "lines": []
    }

    with pytest.raises(Exception):
        FigureInterface(figure_data)

