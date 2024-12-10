# START:

import matplotlib.pyplot as plt


class AtomicWeights:
    """
    A class to handle the creation of pie charts based on atomic weights of elements.
    Attributes:
        atomic_weights (list): List of atomic weights for the first six elements.
    """

    # Class variable with atomic weights of the first six elements (Hydrogen, Helium, Lithium, Beryllium, Boron, Carbon)
    atomic_weights = [1, 4, 7, 9, 11, 12]

    def create_pie_chart(self, element1, element2):
        """
        Creates two pie charts for given elements with annotations of percentages and atomic weights.
        Explodes the first element in the first chart and the second in the second chart.

        Args:
            element1 (str): The name of the first element to explode in the pie chart.
            element2 (str): The name of the second element to explode in the pie chart.

        Return:
            None, displays pie charts.
        """

        # List of element names corresponding to the atomic weights
        elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon']
        # Retrieve class variable atomic weights
        weights = AtomicWeights.atomic_weights
        # Create explosion settings for the first pie chart, where the specified element is exploded
        explode1 = [0.1 if element == element1 else 0 for element in elements]
        # Create explosion settings for the second pie chart, where the specified element is exploded
        explode2 = [0.1 if element == element2 else 0 for element in elements]

        # Setup a figure to host two subplots (pie charts) side by side
        fig, ax = plt.subplots(1, 2, figsize = (14, 7))
        # First pie chart: elements with the first specified element exploded
        ax[0].pie(weights, labels=weights, autopct = '%1.1f%%', startangle = 90, explode = explode1)
        # Title reflecting the exploded element
        ax[0].set_title(f'Pie Chart for {element1} Exploded')

        # Second pie chart: elements with the second specified element exploded
        ax[1].pie(weights, labels = weights, autopct = '%1.1f%%', startangle = 90, explode = explode2)
        # Title reflecting the exploded element
        ax[1].set_title(f'Pie Chart for {element2} Exploded')

        # Display the plots
        plt.show()


# MAIN function call
if __name__ == '__main__':
    aw = AtomicWeights()
    aw.create_pie_chart('Hydrogen', 'Carbon')

# END.