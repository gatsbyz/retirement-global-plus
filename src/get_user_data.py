import questionary

def get_retire_plan_user():

    age = questionary.text("What is your current age").ask()
    retirement_age = questionary.text("By what age, would you prefer to retire?").ask()
    savings = questionary.text("How much do you have in liquid cash savings (USD)").ask()
    portfolio_type = questionary.text("Would you like your portfolio to be conservative[1], conservatively moderate[2], or moderate[3]? (Enter 1, 2, or 3)").ask()
    total_stocks_bonds = questionary.text("How much would you like to invest in stocks and bonds?").ask()
        
    age = int(age)
    retirement_age = int(retirement_age)
    savings = float(savings)
    portfolio_type = int(portfolio_type)
    total_stocks_bonds = float(total_stocks_bonds)

    return age, retirement_age, savings, portfolio_type, total_stocks_bonds

def run():
    age, retirement_age, savings, portfolio_type, total_stocks_bonds = get_retire_plan_user()
    age_of_death = int(80)
    retirement_years = int(age_of_death - retirement_age)
    years_to_retirement = int(retirement_age - age)
    
    return retirement_years, years_to_retirement, savings, portfolio_type, total_stocks_bonds
