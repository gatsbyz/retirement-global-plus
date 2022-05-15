
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import os

from MCForecastTools import MCSimulation

import pandas as pd



def create_savings_dataframe(savings, total_stocks_bonds):
    # Step 1: Create a Python list named savings_data that has two elements.
    # The first element contains the total value of the cryptocurrency wallet. 
    # The second element contains the total value of the stock and bond portions of the portfolio.

    # Consolidate financial assets data into a Python list
    savings_data=[]

    savings_data.append(savings)
    savings_data.append(total_stocks_bonds)

    # Step 2: Use the savings_data list to create a Pandas DataFrame named savings_df, and then display this DataFrame.
    # The function to create the DataFrame should take the following three parameters:

    # savings_data: Use the list that you just created.
    # columns: Set this parameter equal to a Python list with a single value called amount.
    # index: Set this parameter equal to a Python list with the values of crypto and stock/bond.

    # Create a Pandas DataFrame called savings_df 
    index=["cash", "stock/bond"]
    columns=["amount"]
    savings_df = pd.DataFrame(savings_data , columns=columns, index=index)
    return savings_df


def get_portfolio_dataframe():
    ### Get data from Alpaca for MC Simulation of retirement portfolio.

    load_dotenv()

    # Set the variables for the Alpaca API and secret keys
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    # Create the Alpaca tradeapi.REST object
    alpaca = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        api_version="v2")

    # Step 3: Make an API call via the Alpaca SDK to get 3 years of historical closing prices for a traditional 60/40 portfolio split:
    # 60% stocks (SPY) and 40% bonds (AGG).

    # Set start and end dates of 3 years back from your current date
    # Alternatively, you can use an end date of 2020-08-07 and work 3 years back from that date 
    start_date = pd.Timestamp("2019-04-22", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2022-04-22", tz="America/New_York").isoformat()

    # Set number of rows to 1000 to retrieve the maximum amount of rows
    limit_rows=10000

    # Use the Alpaca get_bars function to make the API call to get the 3 years worth of pricing data
    # The tickers and timeframe parameters should have been set in Part 1 of this activity 
    # The start and end dates should be updated with the information set above
    # Remember to add the df property to the end of the call so the response is returned as a DataFrame
    timeframe="1Day"
    tickers=["SPY", "AGG"]
    df_portfolio = alpaca.get_bars(
        tickers,
        timeframe,
        start = start_date,
        end = end_date,
        limit=limit_rows
    ).df

    # Reorganize the DataFrame
    # Separate ticker data
    SPY = df_portfolio[df_portfolio['symbol']=='SPY'].drop('symbol', axis=1)
    AGG = df_portfolio[df_portfolio['symbol']=='AGG'].drop('symbol', axis=1)


    # Concatenate the ticker DataFrames
    df_portfolio = pd.concat([SPY,AGG],axis=1, keys=['SPY','AGG'])
    return df_portfolio


# Step 4: Run a Monte Carlo simulation of 500 samples and 30 years for the 60/40 portfolio, and then plot the results.
# Configure the Monte Carlo simulation to forecast 30 years cumulative returns
# The weights should be split 40% to FXNAX and 60% to SPY.
# Run 500 samples.
def run_mc_output(df_portfolio, portfolio_type, years_to_retirement):
    df_portfolio = get_portfolio_dataframe()
    if portfolio_type == 'Moderate':
        MonteCarlo_output = MCSimulation(
            portfolio_data = df_portfolio,
            weights = [.63,.37],
            num_simulation = 500,
            num_trading_days = 252*years_to_retirement)
        
    elif portfolio_type == "Conservative":
        MonteCarlo_output = MCSimulation(
            portfolio_data = df_portfolio,
            weights = [.29,.71],
            num_simulation = 500,
            num_trading_days = 252*years_to_retirement)
        
    else:
        MonteCarlo_output = MCSimulation(
            portfolio_data = df_portfolio,
            weights = [.44,.56],
            num_simulation = 500,
            num_trading_days = 252*years_to_retirement)
    MonteCarlo_output.portfolio_data.dropna()
    return MonteCarlo_output

def summary_statistics(output):
    return output.summarize_cumulative_return()

def mean_cumulative_return(output, total_stocks_bonds):
    return summary_statistics(output)[5] * float(total_stocks_bonds)

def savings_at_retirement(mean_cumulative_return, savings):
    return float(mean_cumulative_return + savings)

def get_retirement_cities(output, data, retirement_years, total_stocks_bonds, savings):

    mean_cumulative_return_val =  mean_cumulative_return(output, total_stocks_bonds)
    savings_at_retirement_val = savings_at_retirement(mean_cumulative_return_val, savings)

    retirement_cities = []
            
    for item in data:
        if savings_at_retirement_val >= (item['estimated_monthly_costs_with_rent'] * (retirement_years * 12)):                
            retirement_cities.append(item['city'] + '/' + item['country']) 

    return retirement_cities