class DatabaseError(Exception):
    """Custom exception for database-related errors."""
    def __init__(self, message="An error occurred with the database."):
        super().__init__(message)


class DataProcessingError(Exception):
    """Custom exception for data processing errors."""
    def __init__(self, message="An error occurred while processing the data."):
        super().__init__(message)


class VisualizationError(Exception):
    """Custom exception for visualization-related errors."""
    def __init__(self, message="An error occurred while generating visualizations."):
        super().__init__(message)
