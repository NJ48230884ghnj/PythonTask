# **Task: Ideal Function Mapping**

## **Summary**
- This project maps training data to the best ideal functions and maps test data to these ideal functions with minimal deviation.
- Includes data visualization for analysis and robust testing for all major functionalities.

---

## **Contents**
- **Database Management**:
  - Loads and manages training, ideal, and test data in an SQLite database.
- **Data Processing**:
  - Identifies the best ideal functions using the Least Squares Method.
  - Maps test data to ideal functions and calculates deviations.
- **Visualization**:
  - Training data vs. Ideal functions.
  - Test data mappings with deviations.
- **Unit Testing**:
  - Comprehensive tests for database operations, data processing, and visualizations.

---

## **Project Layout**
- **`data/`**:
  - `train.csv` - Training data.
  - `ideal.csv` - Ideal functions.
  - `test.csv` - Test data.
- **`output/`**:
  - `assignment.db` - SQLite database for the program.
  - `test_assignment.db` - Temporary database for testing.
- **`src/`**:
  - `database.py` - Handles database setup and operations.
  - `verify_database.py` - Gives output of loaded data 
  - `processing.py` - Data processing logic (e.g., best function mapping).
  - `visualization.py` - Generates visualizations for analysis.
  - `exceptions.py` - Custom exceptions for error handling.
  - `main.py` - Entry point for the program.
- **`tests/`**:
  - `test_database.py` - Tests for database functionality.
  - `test_processing.py` - Tests for data processing.
  - `test_visualization.py` - Tests for visualization functions.
- `README.md` - Project documentation.
- `requirements.txt` - Python dependencies.
- `pytest.ini` - Pytest configuration.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8 or later.
- Virtual environment.

### **Steps**:
1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment:
   - **Linux/Mac**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows**:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt


## Run the Program
```python src/main.py```

### Choose an option:
1. Load Data into Database.
2. Process Data (Map training/test data).
3. Visualize Results.

## Testing

- To verify the functionality of the program:
bash
Copy code

```pytest tests/```


## Visualization

### Training Data vs. Ideal Functions
- Visualizes how well the training data matches the ideal functions.
### Test Data Mappings
- Shows test data mapped to the ideal functions with deviation annotations.

