from database import DatabaseHandler
from processing import DataProcessor
from visualization import Visualizer
import pandas as pd


def load_data_into_database():
    """
    Loads data from CSV files into the SQLite database using DatabaseHandler.
    """
    # Initialize the DatabaseHandler
    db_handler = DatabaseHandler()

    # Create the database tables
    db_handler.create_tables()

    # Load data from CSV files
    try:
        train_data = pd.read_csv("data/train.csv")
        ideal_data = pd.read_csv("data/ideal.csv")
        test_data = pd.read_csv("data/test.csv")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # Insert data into the respective tables
    try:
        db_handler.insert_data("training_data", train_data)
        print("Train Data successfully loaded into the database.")
        print("Train Data (head):")
        print(train_data.head())
        print('*' * 10)
        print(train_data.info)
        print('*' * 10)
        print(train_data.describe())

        db_handler.insert_data("ideal_functions", ideal_data)
        print("\nIdeal Data successfully loaded into the database.")
        print("Ideal Data (head):")
        print(ideal_data.head())
        print('*' * 10)
        print(ideal_data.info)
        print('*' * 10)
        print(ideal_data.describe())
        

        db_handler.insert_data("test_data", test_data)
        print("\nTest Data successfully loaded into the database.")
        print("Test Data (head):")
        print(test_data.head())
        print('*' * 10)
        print(test_data.info)
        print('*' * 10)
        print(test_data.describe())

    except Exception as e:
        print(f"Error inserting data into the database: {e}")



def process_data():
    """
    Processes data to find best ideal functions and map test data.
    """
    db_handler = DatabaseHandler()

    # Fetch data from the database
    training_data = db_handler.fetch_data("training_data")
    ideal_data = db_handler.fetch_data("ideal_functions")
    test_data = db_handler.fetch_data("test_data")

    # Initialize DataProcessor
    processor = DataProcessor(training_data, ideal_data)

    # Find the best ideal functions
    best_functions = processor.find_best_ideal_functions()
    print("\nBest Ideal Functions Mapping:")
    for train_col, ideal_col in best_functions.items():
        print(f"{train_col} -> {ideal_col}")

    # Map the test data
    mapped_test_data = processor.map_test_data(test_data, best_functions)
    print("\nMapped Test Data:")
    print(mapped_test_data.head())

    # Save the mapped test data to the database
    db_handler.insert_data("test_mappings", mapped_test_data)

def visualize_results():
    """
    Visualizes the results using the Visualizer class.
    """
    db_handler = DatabaseHandler()

    # Fetch data from the database
    training_data = db_handler.fetch_data("training_data")
    ideal_data = db_handler.fetch_data("ideal_functions")
    test_mappings = db_handler.fetch_data("test_mappings")

    # Find the best functions mapping from the database
    processor = DataProcessor(training_data, ideal_data)
    best_functions = processor.find_best_ideal_functions()

    # Initialize the Visualizer
    visualizer = Visualizer()

    # Plot training vs. ideal functions
    visualizer.plot_training_vs_ideal(training_data, ideal_data, best_functions)

    # Plot test data mappings
    visualizer.plot_test_mappings(test_mappings)


if __name__ == "__main__":
    print("1. Load Data into Database")
    print("2. Process Data")
    print("3. Visualize Results")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        load_data_into_database()
    elif choice == "2":
        process_data()
    elif choice == "3":
        visualize_results()
    else:
        print("Invalid choice. Please run the script again.")
        
