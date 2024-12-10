# START:

import pandas as pd
import matplotlib.pyplot as plt


def my_charts(filename):
    """
    Reads a CSV file and creates both a horizontal and a vertical bar chart of the data.

    Args:
        filename (str): Path to the CSV file to read.

    Return:
        None, displays bar charts.
    """

    # Load the CSV file into a DataFrame.
    data = pd.read_csv(filename)

    # Set up the figure for a horizontal bar chart.
    plt.figure(figsize = (10, 6))
    # Create a horizontal bar chart using 'Adoption' rates as bars and 'IDE' as categories.
    plt.barh(data['IDE'], data['Adoption'])
    # Label for the x-axis.
    plt.xlabel('Adoption Rate')
    # Title of the chart.
    plt.title('Horizontal Bar Chart of IDE Adoption')
    # Display the chart.
    plt.show()

    # Set up the figure for a vertical bar chart with the same size as above.
    plt.figure(figsize = (10, 6))
    # Create a vertical bar chart, which uses 'IDE' as the x-axis categories and 'Adoption' rates for the bars.
    plt.bar(data['IDE'], data['Adoption'])
    # Label for the y-axis.
    plt.ylabel('Adoption Rate')
    # Rotate the category labels (IDE names) on the x-axis for better readability.
    plt.xticks(rotation = 45)
    # Title of the chart.
    plt.title('Vertical Bar Chart of IDE Adoption')
    # Display the chart.
    plt.show()


# MAIN function call
if __name__ == '__main__':
    my_charts('py_ide2.csv')

# END.