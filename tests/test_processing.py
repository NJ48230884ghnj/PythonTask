import pytest
import pandas as pd
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from processing import DataProcessor  # In test_processing.py

@pytest.fixture
def mock_data():
    # Mock data for testing
    training_data = pd.DataFrame({"x": [1, 2, 3], "y1": [1, 4, 9], "y2": [2, 5, 10]})
    ideal_data = pd.DataFrame({"x": [1, 2, 3], "y1": [1.1, 3.9, 9.2], "y2": [1.9, 5.1, 10.3]})
    return training_data, ideal_data

def test_find_best_ideal_functions(mock_data):
    training_data, ideal_data = mock_data
    processor = DataProcessor(training_data, ideal_data)
    
    best_functions = processor.find_best_ideal_functions()
    assert best_functions == {"y1": "y1", "y2": "y2"}  # Example expected mapping

def test_map_test_data(mock_data):
    training_data, ideal_data = mock_data
    test_data = pd.DataFrame({"x": [1, 2, 3], "y": [1.05, 4.1, 9.9]})
    processor = DataProcessor(training_data, ideal_data)
    best_functions = {"y1": "y1"}
    
    mapped_data = processor.map_test_data(test_data, best_functions)
    assert not mapped_data.empty  # Ensure the output is not empty
    assert "ideal_function" in mapped_data.columns
    assert "deviation" in mapped_data.columns
