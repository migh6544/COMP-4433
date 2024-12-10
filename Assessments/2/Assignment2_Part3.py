# START:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def values_dates():
    """
    Creates a DataFrame from a list of dates and random values and plots them as a line and a bar chart.

    Args:
        None

    Return:
        None, displays charts.
    """

    # Generate a range of dates starting from January 1, 2024. It generates 8 dates spaced 30 days apart.
    dates = pd.date_range(start = '2024-01-01', periods = 8, freq = '30D')

    # Generate 8 random values uniformly distributed between 100 and 200.
    values = np.random.uniform(low = 100, high = 200, size = 8)

    # Create a DataFrame using the generated values with the dates as the index.
    df = pd.DataFrame({'Value': values}, index = dates)

    # Start plotting the data. This sets up a figure with enough space for two subplots (one line plot and one bar chart).
    plt.figure(figsize = (14, 7))

    # Create a line plot in the first subplot position (1 row, 2 columns, position 1).
    plt.subplot(1, 2, 1)
    plt.plot(df.index, df['Value'], marker='o')
    # Title for the line plot
    plt.title('Line Plot of Values vs Dates')
    # Label for the x-axis
    plt.xlabel('Date')
    # Label for the y-axis
    plt.ylabel('Value')

    # Create a bar chart in the second subplot position to visualize the same data as a series of bars.
    plt.subplot(1, 2, 2)
    # The width is set to 10 days for clarity in visualization.
    plt.bar(df.index, df['Value'], width=10)
    # Title for the bar chart
    plt.title('Bar Chart of Values vs Dates')
    # Label for the x-axis
    plt.xlabel('Date')
    # Label for the y-axis
    plt.ylabel('Value')

    # Adjust the layout to make sure there is no overlap and everything fits nicely.
    plt.tight_layout()
    plt.show()


# MAIN function call
if __name__ == '__main__':
    values_dates()

# END.