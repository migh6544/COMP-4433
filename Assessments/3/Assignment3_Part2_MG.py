## START:


import seaborn as sns
import matplotlib.pyplot as plt


def my_precious(color1, color2):
    """
    Generate a FacetGrid with scatterplots of 'price' vs. 'carat'
    for the Seaborn dataset 'diamonds', filtering based on provided colors.

    Parameters:
        color1 (str): First color grade for diamonds (uppercase letter).
        color2 (str): Second color grade for diamonds (uppercase letter).
    """
    # Load the dataset
    diamonds = sns.load_dataset('diamonds')

    # Filter the dataset
    diamonds_filtered = diamonds[(diamonds['cut'] != 'Fair') & (~diamonds['color'].isin([color1, color2]))]

    # Create FacetGrid
    g = sns.FacetGrid(diamonds_filtered, col = 'cut', row = 'color', margin_titles = True)

    # Plot scatterplot
    g.map(sns.scatterplot, 'carat', 'price')
    plt.subplots_adjust(top = 0.9)
    g.figure.suptitle('Price vs. Carat for Diamonds (Filtered)')
    plt.show()

def main():
    """Main function to execute my_precious."""
    color1 = 'D'
    color2 = 'E'
    my_precious(color1, color2)


if __name__ == "__main__":
    main()


## END.