import numpy as np
import pandas as pd

class DataProcessor:
    """
    Handles data analysis for finding ideal functions and mapping test data.
    """

    def __init__(self, training_data, ideal_data):
        """
        Initializes the DataProcessor with training and ideal function data.
        
        Args:
            training_data (pd.DataFrame): Training data with columns 'x', 'y1', 'y2', ...
            ideal_data (pd.DataFrame): Ideal functions with columns 'x', 'y1', 'y2', ...
        """
        self.training_data = training_data
        self.ideal_data = ideal_data

    def find_best_ideal_functions(self):
        """
        Identifies the best ideal functions for each training data column using the Least Squares Method.

        Returns:
            dict: Mapping of training column (e.g., 'y1') to ideal function column (e.g., 'y10').
        """
        best_functions = {}

        # Loop over each training column (y1, y2, ...)
        for train_col in self.training_data.columns[1:]:
            min_error = float('inf')
            best_function = None

            # Loop over each ideal function column (y1, y2, ...)
            for ideal_col in self.ideal_data.columns[1:]:
                # Calculate the sum of squared differences (Least Squares Error)
                error = np.sum((self.training_data[train_col] - self.ideal_data[ideal_col]) ** 2)
                if error < min_error:
                    min_error = error
                    best_function = ideal_col

            best_functions[train_col] = best_function

        return best_functions

    def map_test_data(self, test_data, best_functions):
        """
        Maps test data points to ideal functions based on minimum deviation within a threshold.
        
        Args:
            test_data (pd.DataFrame): Test data with columns 'x', 'y'.
            best_functions (dict): Mapping of training columns to ideal functions.

        Returns:
            pd.DataFrame: Mapped test data with columns ['x', 'y', 'ideal_function', 'deviation'].
        """
        mapped_data = []

        # Compute max deviations for each ideal function
        max_deviations = {}
        for train_col, ideal_col in best_functions.items():
            max_deviations[ideal_col] = np.max(
                np.abs(self.training_data[train_col] - self.ideal_data[ideal_col])
            )

        threshold_factor = np.sqrt(2)

        # Map each test data point
        for _, row in test_data.iterrows():
            x, y = row["x"], row["y"]
            best_mapping = None
            min_deviation = float('inf')

            for train_col, ideal_col in best_functions.items():
                # Find the corresponding ideal function value for this x
                ideal_y = self.ideal_data.loc[self.ideal_data["x"] == x, ideal_col]
                if ideal_y.empty:
                    continue
                deviation = abs(y - ideal_y.values[0])

                # Check if deviation is within the threshold
                if deviation <= threshold_factor * max_deviations[ideal_col]:
                    if deviation < min_deviation:
                        min_deviation = deviation
                        best_mapping = (x, y, ideal_col, deviation)

            if best_mapping:
                mapped_data.append(best_mapping)

        # Create a DataFrame for the mapped test data
        return pd.DataFrame(mapped_data, columns=["x", "y", "ideal_function", "deviation"])
