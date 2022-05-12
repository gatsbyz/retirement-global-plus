import sys
from tkinter import Y
import fire
import questionary
from pathlib import Path

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
#retirement_years = int(age_of_death - retirement_age)
#years_to_retirement = int(retirement_age - age)
#total_stocks_bonds = float(stock_portfolio_amount + bond_portfolio_amount)

age, retirement_age, savings, portfolio_type, stock_portfolio_amount, bond_portfolio_amount = get_retire_plan()