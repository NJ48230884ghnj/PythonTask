import pytest
import pandas as pd
from unittest.mock import patch
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from processing import DataProcessor  # In test_processing.py
from visualization import Visualizer  # 

@pytest.fixture
def mock_data():
    training_data = pd.DataFrame({"x": [1, 2, 3], "y1": [1, 4, 9]})
    ideal_data = pd.DataFrame({"x": [1, 2, 3], "y1": [1.1, 3.9, 9.2]})
    test_mappings = pd.DataFrame({
        "x": [1, 2, 3],
        "y": [1.05, 4.1, 9.9],
        "ideal_function": ["y1", "y1", "y1"],
        "deviation": [0.05, 0.1, 0.1]
    })
    best_functions = {"y1": "y1"}
    return training_data, ideal_data, test_mappings, best_functions

@patch("matplotlib.pyplot.show")
def test_plot_training_vs_ideal(mock_show, mock_data):
    training_data, ideal_data, _, best_functions = mock_data
    visualizer = Visualizer()
    
    # Call the function and ensure no exceptions are raised
    visualizer.plot_training_vs_ideal(training_data, ideal_data, best_functions)
    mock_show.assert_called_once()

@patch("matplotlib.pyplot.show")
def test_plot_test_mappings(mock_show, mock_data):
    _, _, test_mappings, _ = mock_data
    visualizer = Visualizer()
    
    # Call the function and ensure no exceptions are raised
    visualizer.plot_test_mappings(test_mappings)
    mock_show.assert_called_once()
