# START:

import pandas as pd
import numpy as np



## Part 1
# Function to write the initial CSV file for elements
def create_csv():
    """
    Creates a CSV file named 'elements.csv' with the first eight elements of the periodic table.
    The columns include name, symbol, and atomic_number.
    """

    elements = [
        {'name': 'Hydrogen', 'symbol': 'H', 'atomic_number': 1},
        {'name': 'Helium', 'symbol': 'He', 'atomic_number': 2},
        {'name': 'Lithium', 'symbol': 'Li', 'atomic_number': 3},
        {'name': 'Beryllium', 'symbol': 'Be', 'atomic_number': 4},
        {'name': 'Boron', 'symbol': 'B', 'atomic_number': 5},
        {'name': 'Carbon', 'symbol': 'C', 'atomic_number': 6},
        {'name': 'Nitrogen', 'symbol': 'N', 'atomic_number': 7},
        {'name': 'Oxygen', 'symbol': 'O', 'atomic_number': 8},
    ]
    df = pd.DataFrame(elements)
    df.to_csv('elements.csv', index = False)

# Function to read the elements CSV and modify it
def atomic_elements(fileName):
    """
    Reads a CSV file into a pandas DataFrame, adds additional elements, and a column for atomic weights.
    Checks for any NaN values in the atomic_weight column and replaces them with the correct atomic weights.
    All atomic weights are rounded to the nearest integer.

    Args:
    - fileName: String. The name of the CSV file to read.

    Returns:
    - A pandas DataFrame with the updated elements list and corrected atomic weights.
    """

    df = pd.read_csv(fileName)

    # Adding 9th and 10th elements if not already present
    additionalElements = pd.DataFrame([
        {'name': 'Fluorine', 'symbol': 'F', 'atomic_number': 9},
        {'name': 'Neon', 'symbol': 'Ne', 'atomic_number': 10}
    ])
    df = pd.concat([df, additionalElements], ignore_index = True)

    # Atomic weights dictionary
    atomicWeights = {
        'Hydrogen': 1,    # Actual: ~1.008
        'Helium': 4,      # Actual: ~4.0026
        'Lithium': 7,     # Actual: ~6.94
        'Beryllium': 9,   # Actual: ~9.0122
        'Boron': 11,      # Actual: ~10.81
        'Carbon': 12,     # Actual: ~12.011
        'Nitrogen': 14,   # Actual: ~14.007
        'Oxygen': 16,     # Actual: ~15.999
        'Fluorine': 19,   # Actual: ~18.998
        'Neon': 20        # Actual: ~20.180
    }

    # Check and replace NaN in atomic_weight with correct values, rounded to the nearest integer
    if 'atomic_weight' not in df.columns or df['atomic_weight'].isnull().any():
        df['atomic_weight'] = df['name'].apply(lambda x: atomicWeights.get(x))

    # Ensure atomic_weight column is of integer type
    df['atomic_weight'] = df['atomic_weight'].astype(int)

    return df


## Part 2
def arr_to_df():
    """
    Creates a DataFrame from multiple sources of data, including Greek letters and numerical arrays generated with numpy.

    This function performs several operations:
    - Constructs a list of nine Greek letters not in alphabetical order.
    - Generates two 9-element numpy arrays of random floating-point numbers, aiming for a mean of 10 and a standard deviation of 1.5.
    - Creates an array of nine evenly spaced angles ranging from 0 to 2*pi.
    - Calculates the cosine for each of the angles to form another array.
    - Combines all above data into a pandas DataFrame.
    - Sorts the DataFrame in ascending order based on the Greek letters.
    - Drops two columns of choice and one of the rows from the sorted DataFrame.

    Returns:
        pandas.DataFrame: A modified DataFrame containing selected Greek letters, angles, and cosines, sorted by Greek letter,
                          with specific columns and a row removed.
    """

    greekLetters = ['delta', 'alpha', 'gamma', 'epsilon', 'beta', 'zeta', 'eta', 'theta', 'iota']
    arr1 = np.random.normal(10, 1.5, 9)
    arr2 = np.random.normal(10, 1.5, 9)
    angle = np.linspace(0, 2 * np.pi, 9)
    cosine = np.cos(angle)
    dataDict = {
        'Greek Letter': greekLetters,
        'Array 1': arr1,
        'Array 2': arr2,
        'Angle': angle,
        'Cosine': cosine
    }
    df = pd.DataFrame(dataDict)
    print(f"\n--* Part 2 *--\n\n{df}\n")
    dfSorted = df.sort_values(by='Greek Letter')
    dfModified = dfSorted.drop(['Array 1', 'Array 2'], axis=1).drop(dfSorted.index[0])
    return dfModified

## Part 3
def fib():
    """
    Generates a list of the first 12 Fibonacci numbers starting from 1 and calculates the ratio of each number to its predecessor for the last five numbers.

    Returns:
        list: A list containing the ratios of each of the last five Fibonacci numbers to its predecessor.
    """

    fibNumbers = [1, 1]
    for i in range(2, 12):
        nextNumber = fibNumbers[-1] + fibNumbers[-2]
        fibNumbers.append(nextNumber)
    ratios = [fibNumbers[i] / fibNumbers[i - 1] for i in range(-5, 0)]
    return ratios

## Part 4
def k_to_r(kelvin):
    """
    Converts a given temperature from Kelvin to Rankine.

    Args:
    - kelvin (float): The temperature in Kelvin.

    Returns:
    - float: The temperature converted to Rankine.
    """

    return kelvin * (9/5)


def main():
    # Ensuring the last command in terminal is separated from the output for improved readability
    print("\n\n\n---*** Assignment 1: Michael Ghattas ***---\n")
    # Part 1 Execution: Create the CSV file first
    create_csv()

    # Now, read and modify the CSV file with additional elements and atomic weights
    df_elements = atomic_elements('elements.csv')
    print(f"\n--* Part 1 *--\n\n{df_elements}\n")


    # Part 2 Execution
    df_arr = arr_to_df()
    print(f"{df_arr}\n")


    # Part 3 Execution
    fibonacciRatios = fib()
    print(f"\n--* Part 3 *--\n\nFibonacci Ratios", f"\n{fibonacciRatios}\n-> These ratios highlight the mathematical properties of the Fibonacci sequence, specifically its relationship to the golden ratio (~1.618)")


    # Part 4 Execution
    kelvinTemperatures = [273.15, 310.15, 0, 100, 373.15]
    print(f"\n--* Part 4 *--\n\n- Conversion using the function -")
    for temp in kelvinTemperatures:
        print(f"{temp}K = {k_to_r(temp)}R")

    print("\n- Conversion using a lambda function -")
    k_to_r_lambda = lambda k: k * (9/5)
    for temp in kelvinTemperatures:
        print(f"{temp}K = {k_to_r_lambda(temp)}R")



if __name__ == "__main__":
    main()
    print("\n\n")

# END.