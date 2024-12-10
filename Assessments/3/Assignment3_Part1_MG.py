## START:


import seaborn as sns
import matplotlib.pyplot as plt


def autompg():
    """
    Generate a heatmap of the correlation of all numeric columns
    and a pairplot of the same for the Seaborn dataset 'mpg'.
    """
    # Load the dataset
    mpg = sns.load_dataset('mpg')

    # Heatmap of correlation
    plt.figure(figsize=(10, 6))
    sns.heatmap(mpg.corr(), annot = True, cmap = 'coolwarm', fmt = ".2f")
    plt.title('Correlation Heatmap of MPG Dataset')
    plt.show()

    # Pairplot
    sns.pairplot(mpg)
    plt.title('Pairplot of MPG Dataset')
    plt.show()

def main():
    """Main function to execute autompg."""
    autompg()


if __name__ == "__main__":
    main()


## END.