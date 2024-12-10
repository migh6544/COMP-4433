# Start:

import yfinance as yf
import matplotlib.pyplot as plt


class YahooFinance:
    """
    Class to handle stock data retrieval and plotting for a given ticker and duration using Yahoo Finance API.

    Attributes:
        ticker (str): Ticker symbol of the stock.
        duration (str): Duration to retrieve data, default is '1mo'.
        company_df (DataFrame): DataFrame storing the stock data.
    """

    def __init__(self, ticker, duration='1mo'):
        """
        Initializes the YahooFinance class with ticker and duration.

        Args:
            ticker (str): Ticker symbol for the stock.
            duration (str): Duration to retrieve data, default to '1mo' for one month of data.
        """

        # Store the ticker symbol for future reference
        self.ticker = ticker
        # Store the data retrieval duration
        self.duration = duration
        # Automatically load data on initialization
        self.load_data()

    def load_data(self):
        """
        Retrieves stock data from Yahoo Finance and stores it in company_df.

        Args:
            None

        Return:
            None
        """

        # Initialize a Ticker object from yfinance with the given ticker symbol
        stock = yf.Ticker(self.ticker)
        # Retrieve historical market data based on the specified duration
        self.company_df = stock.history(period=self.duration)

    def plot_data(self):
        """
        Plots the closing prices and volumes of the stock on two separate subplots.

        Args:
            None

        Return:
            None, displays a plot.
        """

        # Create a subplot with 2 rows for plotting closing prices and trading volumes
        fig, ax = plt.subplots(2, 1, figsize = (12, 10), sharex = True)

        # Plotting the closing prices
        ax[0].plot(self.company_df.index, self.company_df['Close'], label = 'Close Price')
        # Title using the ticker symbol
        ax[0].set_title(f'Closing Prices for {self.ticker}')
        # Y-axis label for prices
        ax[0].set_ylabel('Price ($)')
        # Legend positioned in the upper left
        ax[0].legend(loc='upper left')

        # Plotting the trading volumes
        ax[1].bar(self.company_df.index, self.company_df['Volume'], color = 'orange', label = 'Volume')
        # Title using the ticker symbol
        ax[1].set_title(f'Trading Volume for {self.ticker}')
        # X-axis label for both subplots
        ax[1].set_xlabel('Date')
        # Y-axis label for volume
        ax[1].set_ylabel('Volume')
        # Legend positioned in the upper left
        ax[1].legend(loc='upper left')

        # Adjust layout to prevent overlap
        plt.tight_layout()
        plt.show()


# MAIN function call
if __name__ == '__main__':
    finance = YahooFinance('AAPL')
    finance.plot_data()

#END.