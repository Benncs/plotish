import pytest
from plotish import LineInterface

def test_line_interface_creation():
    # Test creating LineInterface instance
    line_data = {
        "color": "blue",
        "style": "--",
        "legend": "Test Line",
        "marker": "o",
        "xdata": [1, 2, 3],
        "ydata": [4, 5, 6]
    }
    line_instance = LineInterface(line_data)

    # Assert properties are set correctly
    assert line_instance.data.tolist() == [[1, 2, 3], [4, 5, 6]]
    assert line_instance.kwargs == {"color": "blue", "linestyle": "--", "label": "Test Line", "marker": "o"}

def test_line_interface_no_ydata():
    # Test creating LineInterface instance with no ydata (should raise an exception)
    line_data = {
        "color": "red",
        "style": "-",
        "legend": "No YData Line",
        "marker": "x",
        "xdata": [1, 2, 3],
    }

    with pytest.raises(Exception):
        LineInterface(line_data)

