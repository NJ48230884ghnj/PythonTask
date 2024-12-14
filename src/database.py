from sqlalchemy import create_engine, Table, Column, Float, MetaData
import pandas as pd

class DatabaseHandler:
    """
    Handles all database operations, including table creation, data insertion, and data retrieval.
    """
    def __init__(self, db_path="output/assignment.db"):
        """
        Initializes the DatabaseHandler with a SQLite database connection.
        
        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.metadata = MetaData()

    def create_tables(self):
        """
        Creates necessary tables in the SQLite database:
        - training_data
        - ideal_functions
        - test_data
        - test_mappings
        """
        self.training_table = Table("training_data", self.metadata,
                                    Column("x", Float),
                                    Column("y1", Float),
                                    Column("y2", Float),
                                    Column("y3", Float),
                                    Column("y4", Float))
        self.ideal_table = Table("ideal_functions", self.metadata,
                                 Column("x", Float),
                                 *(Column(f"y{i+1}", Float) for i in range(50)))
        self.test_table = Table("test_data", self.metadata,
                                Column("x", Float),
                                Column("y", Float))
        self.mappings_table = Table("test_mappings", self.metadata,
                                    Column("x", Float),
                                    Column("y", Float),
                                    Column("ideal_function", Float),
                                    Column("deviation", Float))
        self.metadata.create_all(self.engine)

    def insert_data(self, table_name, dataframe):
        """
        Inserts data into the specified table from a Pandas DataFrame.
        
        Args:
            table_name (str): Name of the table to insert data into.
            dataframe (pd.DataFrame): DataFrame containing the data to insert.
        """
        dataframe.to_sql(table_name, self.engine, if_exists="replace", index=False)

    def fetch_data(self, table_name):
        """
        Fetches data from the specified table as a Pandas DataFrame.
        
        Args:
            table_name (str): Name of the table to fetch data from.
        
        Returns:
            pd.DataFrame: DataFrame containing the fetched data.
        """
        return pd.read_sql_table(table_name, self.engine)
