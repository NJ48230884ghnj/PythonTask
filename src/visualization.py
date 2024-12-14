import matplotlib.pyplot as plt
import random
import seaborn as sns



class Visualizer:
    """
    Handles data visualization for training data, ideal functions, and test mappings.
    """


    
    def __init__(self):
        pass

    def plot_training_vs_ideal(self, training_data, ideal_data, best_functions):
        """
        Plots training data columns against their corresponding ideal functions.

        Args:
            training_data (pd.DataFrame): Training data with 'x', 'y1', 'y2', ...
            ideal_data (pd.DataFrame): Ideal functions with 'x', 'y1', 'y2', ...
            best_functions (dict): Mapping of training columns to ideal functions.
        """
        plt.figure(figsize=(12, 8))
        
        for train_col, ideal_func in best_functions.items():
            # Plot training data
            plt.plot(
                training_data["x"],
                training_data[train_col],
                label=f"{train_col} (Training)",
                marker="o",
                linestyle="-",
                alpha=0.7,
            )
            # Plot ideal function
            plt.plot(
                ideal_data["x"],
                ideal_data[ideal_func],
                label=f"{ideal_func} (Ideal)",
                linestyle="--",
                alpha=0.7,
            )

        plt.title("Training Data vs. Ideal Functions")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.grid()
        plt.show()

    def plot_test_mappings(self, test_mappings, top_n_labels=5):
        """
        Plots test data points mapped to ideal functions with deviations.

        Args:
            test_mappings (pd.DataFrame): Mapped test data with 'x', 'y', 'ideal_function', 'deviation'.
            top_n_labels (int): Number of points with the highest deviations to label.
        """
        plt.figure(figsize=(12, 8))

        # Use Seaborn's color palette for distinct colors
        ideal_functions = test_mappings["ideal_function"].unique()
        palette = sns.color_palette("tab10", len(ideal_functions))
        colors = {func: palette[i] for i, func in enumerate(ideal_functions)}

        # Plot all points
        for _, row in test_mappings.iterrows():
            x, y, ideal_func, deviation = row["x"], row["y"], row["ideal_function"], row["deviation"]
            plt.scatter(
                x, y, color=colors[ideal_func], alpha=0.7, label=f"{ideal_func}" if f"{ideal_func}" not in plt.gca().get_legend_handles_labels()[1] else ""
            )

        # Highlight and label the points with the top deviations
        top_deviation_points = test_mappings.nlargest(top_n_labels, "deviation")
        for _, row in top_deviation_points.iterrows():
            x, y, ideal_func, deviation = row["x"], row["y"], row["ideal_function"], row["deviation"]

            # Dynamically adjust label placement based on the point's position
            offset_x = 20 if x > 0 else -30
            offset_y = 30 if y > 0 else -30

            plt.scatter(x, y, color=colors[ideal_func], edgecolor="black", s=100, zorder=3)
            plt.annotate(
                f"{ideal_func}\nΔ={deviation:.3f}",
                xy=(x, y),
                xytext=(offset_x, offset_y),
                textcoords="offset points",
                arrowprops=dict(arrowstyle="->", color="black", lw=1),
                fontsize=8,
                ha="center"
            )

        plt.title("Test Data Mappings and Deviations")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid()
        plt.legend(title="Ideal Functions", loc="upper left")
        plt.tight_layout()
        plt.show()