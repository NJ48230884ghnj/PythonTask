import sys
import os
import pytest
import pandas as pd
from sqlalchemy import inspect

# Add the `src` directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from database import DatabaseHandler  # Import the DatabaseHandler class

@pytest.fixture
def db_handler():
    """
    Fixture to initialize the DatabaseHandler for testing.
    It creates a temporary SQLite database for test purposes.
    """
    return DatabaseHandler(db_path="output/test_assignment.db")

def test_create_tables(db_handler):
    """
    Test the creation of database tables.
    Verifies that all required tables are created successfully.
    """
    db_handler.create_tables()
    inspector = inspect(db_handler.engine)  # Use the Inspector to check table existence

    # Verify tables exist
    assert "training_data" in inspector.get_table_names()
    assert "ideal_functions" in inspector.get_table_names()
    assert "test_data" in inspector.get_table_names()
    assert "test_mappings" in inspector.get_table_names()

def test_insert_and_fetch_data(db_handler):
    """
    Test inserting data into and fetching data from the database.
    Uses a sample DataFrame for testing purposes.
    """
    db_handler.create_tables()

    # Create a sample DataFrame
    test_data = pd.DataFrame({
        "x": [1.0, 2.0],
        "y1": [3.0, 4.0],
        "y2": [5.0, 6.0],
        "y3": [7.0, 8.0],
        "y4": [9.0, 10.0]
    })

    # Insert the sample DataFrame into the "training_data" table
    db_handler.insert_data("training_data", test_data)

    # Fetch the data back from the database
    fetched_data = db_handler.fetch_data("training_data")

    # Verify that the inserted data matches the fetched data
    pd.testing.assert_frame_equal(test_data, fetched_data)
