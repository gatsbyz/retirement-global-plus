# Import the required libraries and dependencies
import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as paca
from MCForecastTools import MCSimulation
%matplotlib inline

##REGGIE'S PORTION OF CODE##

# Inputs

#age = input(int("What is your current age?")
#retirement_age = input(int("When would you like to retire?")
#age_of_death = 80
#retirement_years = age_of_death - retirement_age
#years_to_retirment = retirement_age - age
#savings = input(int("How much do you have in your savings account today?")
#cost_of_living = #listofcitieswithcostofliving
#portfolio_type = input(int("Would you like your portfolio to be conservative, conservatively moderate, or moderate?"))
#stock_portoflio_$amount =input(int("How much do you have in your stock account?")
#bond_portoflio_$amount =input(int("How much do you have in your bond account?")

def get_retire_plan():

    age = questionary.text("What is your current age").ask()
    retirement_age = questionary.text("By what age, would you prefer to retire?").ask()
    savings = questionary.text("How much do you have in liquid cash savings (USD)").ask()
    portfolio_type = questionary.text("Would you like your portfolio to be conservative[1], conservatively moderate[2], or moderate[3]? (Enter 1, 2, or 3)").ask()
    stock_portfolio_amount = questionary.text("What is the total cash value of stock holdings?").ask()
    bond_portfolio_amount = questionary.text("What is the total cash value of bond holdings?").ask()
        
    age = int(age)
    retirement_age = int(retirement_age)
    savings = float(savings)
    portfolio_type = int(portfolio_type)
    stock_portfolio_amount = float(stock_portfolio_amount)
    bond_portfolio_amount = float(bond_portfolio_amount)

    return age, retirement_age, savings, portfolio_type, stock_portfolio_amount, bond_portfolio_amount

age_of_death = int(80)
retirement_years = int(age_of_death - retirement_age)
years_to_retirement = int(retirement_age - age)
total_stocks_bonds = float(stock_portfolio_amount + bond_portfolio_amount)

def save_csv (csvpath, data, header="Your Optimized Plan by Retirement Global+"):
    """Saves the CSV file from path provided.

    Arguments:
        csvpath (Path): The CSV file path.
        data (list of lists): A list of cities, where user can retire
        header (list): Added title for branding and brand awareness

    """
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data)


def save_retire_plan(retirement_cities):
    """Saves the qualifying loans to a CSV file.
    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    #This line of code (below) will ask the user if they want to save output to csv file
    #A new variable is created to capture the response from the client
    save_to_file = questionary.text("Would you like to save qualifying loans to a CSV?(yes/no)").ask()
    save_to_file = (save_to_file)

    # "if" statement is introduced in order to account for dynamic response / dialogue
    if save_to_file == "yes":
        csvpath = questionary.text("Enter a file path for qualifying loans (.csv):").ask()
        csvpath = Path(csvpath)

        save_csv(csvpath, qualifying_loans)

def run_app():
    """The main function for running the script."""

    # Get the applicant's information
    age, retirement_age, savings, portfolio_type, stock_portfolio_amount, bond_portfolio_amount = get_retire_plan()

    # Save retirement cities to a .CSV file
    save_retire_plan(retirement_cities)

if __name__ == "__main__":
    fire.Fire(run_app)