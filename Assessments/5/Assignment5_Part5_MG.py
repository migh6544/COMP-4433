## START:

import plotly.graph_objects as go
import numpy as np

def random_hist(n):
    """
    Generates n points from an exponential distribution and plots a histogram using Plotly.

    Args:
        n (int): The number of points to generate.

    Returns:
        None
    """

    # Generate n points from an exponential distribution
    data = np.random.exponential(scale = 1.0, size = n)

    # Create a histogram with at least 15 bins with counts greater than zero
    fig = go.Figure(data = [go.Histogram(x = data, nbinsx = 50)])

    # Update layout for better visualization
    fig.update_layout(
        title = 'Random Exponential Distribution Histogram',
        xaxis_title = 'Value',
        yaxis_title = 'Count'
    )

    # Show the plot
    fig.show()

if __name__ == '__main__':
    random_hist(1000)

## END.