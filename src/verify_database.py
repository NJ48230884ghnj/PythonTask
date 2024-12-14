from database import DatabaseHandler

def verify_data():
    """
    Fetches and prints data from the database to verify if it was loaded correctly.
    """
    # Initialize the DatabaseHandler
    db_handler = DatabaseHandler()

    # Fetch data from each table
    try:
        training_data = db_handler.fetch_data("training_data")
        ideal_functions = db_handler.fetch_data("ideal_functions")
        test_data = db_handler.fetch_data("test_data")
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    # Display the first few rows of each table
    print("\n--- Training Data ---")
    print(training_data.head())

    print("\n--- Ideal Functions ---")
    print(ideal_functions.head())

    print("\n--- Test Data ---")
    print(test_data.head())

if __name__ == "__main__":
    verify_data()
