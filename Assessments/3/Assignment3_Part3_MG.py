## START:


import seaborn as sns
import matplotlib.pyplot as plt


def crashes():
    """
    Generate scattergrams with linear models for 'total' vs. 'speeding'
    and 'total' vs. 'alcohol' for the Seaborn dataset 'car_crashes'.
    """
    # Load the dataset
    car_crashes = sns.load_dataset('car_crashes')

    # Scattergram with linear model for total vs. speeding
    sns.lmplot(x = 'total', y = 'speeding', data = car_crashes)
    plt.title('Total vs. Speeding with Linear Model')
    plt.xlabel('Total Crashes')
    plt.ylabel('Speeding Crashes')
    plt.show()

    # Scattergram with linear model for total vs. alcohol
    sns.lmplot(x = 'total', y = 'alcohol', data = car_crashes)
    plt.title('Total vs. Alcohol with Linear Model')
    plt.xlabel('Total Crashes')
    plt.ylabel('Alcohol-related Crashes')
    plt.show()

def main():
    """Main function to execute crashes."""
    crashes()


if __name__ == "__main__":
    main()


## END.