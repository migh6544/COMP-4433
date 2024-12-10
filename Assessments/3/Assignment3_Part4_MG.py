## START:


import seaborn as sns
import matplotlib.pyplot as plt


def iris():
    """
    Generate a plot with four subplots wherein the distribution of each numeric column
    is presented as a set of boxplots, one for each 'species', for the Seaborn dataset 'iris'.
    """
    # Load the dataset
    iris = sns.load_dataset('iris')

    # Create a figure and axis
    fig, axes = plt.subplots(2, 2, figsize = (10, 8))

    # Plot boxplots for each numeric column for each species
    for i, col in enumerate(iris.columns[:-1]):
        sns.boxplot(x = 'species', y = col, data = iris, ax = axes[i // 2, i % 2])
        axes[i // 2, i % 2].set_title(f'Distribution of {col.capitalize()}')
        axes[i // 2, i % 2].set_xlabel('Species')
        axes[i // 2, i % 2].set_ylabel(col.capitalize())

    plt.tight_layout()
    plt.show()

def main():
    """Main function to execute iris."""
    iris()


if __name__ == "__main__":
    main()


## END.