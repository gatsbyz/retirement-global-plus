# Retirement Global +

## How To Run
0. *open terminal at the root of project1*
1. Run `python3 src/main.py` in terminal to start calculator.
2. Enter your retirement information.
3. Your input will be saved in `cache/user_data.csv`
4. The CLI will show you the cities you can retire in.
5. Your retirement cities will be saved in `cache/retirement-cities.csv`
6. run `jupyter/retirement_tool.ipynb` to visualize your retirement data. the most recent user input will be used.
7. run `jupyter/map_retirement_cities.ipynb` to visualize your retirement cities. the most recent retirement cities will be used.
8. map results saved in `Interactive_retirement_map.html`
9. retire

## Sample Input
? What is your current age 25

? By what age, would you prefer to retire? 65

? How much do you have in liquid cash savings (USD) 50000

? Would you like your portfolio to be conservative[1], conservatively moderate[2], or moderate[3]? 3


? How much would you like to invest in stocks and bonds? 40000

## Sample Output 
You can retire in
['Paris/France', 'Hamilton/Canada', 'Milan/Italy', 'Bucaramanga/Colombia', 'Madrid/Spain', 'Delhi/India']


# Executive Summary

The Retirement Global+ app seeks to flip the script for working citizens around the world. This tool enables users to assess their current assets, as well as their future needs in order to establish an optimized retirement plan to live in any city around the world. The Retirement Global+ app tells you exactly where you can comfortably retire at your preferred retirement age.


# For Users -- General Overview & Flow

Part 1: Data inputs will be generated to determine the years in retirement, size and risk profile of the user's investment portfolio, and historical growth rates of indices.    

Part 2: Users will forecast the performance of their portfolio at the age they wish to retire until the time they choose to retire. Historical price data will be used to generate Monte Carlo simulations to compute total savings (mean) for the time, which elapses btwn the user's current age and the year they prefer to retire.

Part 3: This total cash savings, in addition to asset appreciation will be exported to the Cost of Living Calculator to determine the list of viable cities where the user can retire.

# List of Cities within Scope of Analysis
Hamilton (Bermuda)
<br>
Hong Kong
<br>
Los Angeles
<br>
Paris
<br>
Milan
<br>
Bucaramanga (Colombia)
<br>
Mardrid
<br>
Delhi
<br>
Hamilton (Canada)


---

# Documents

###Team Charter
<br>
https://docs.google.com/document/d/1laAHUYkqxnocPBQqIeRB0HaU6wA8JShfNR4nlD4YaIU/edit?usp=sharing

###Team Presentation (Slides)
<br>
https://docs.google.com/presentation/d/1lwsZ5ntYcasI9LIwBdJl4LitR0IjZjs6vO7VatrjSHk/edit?usp=sharing

---

## Technologies

Required programs, libraries, systems, and overall dependencies:

Python (version 3.0 or later)
<br>
`Pathlib`
<br>
`pandas`
<br>
`%matplotlib`
<br>
`hvplot.pandas`
<br>
`sqlalchemy`
<br>
`numpy`
<br>
`simulation`
<br>
`fileio`
<br>
`questionary`
---

## Installation Guide

`pip install Voila`
<br>
`pip install Fire`
<br>
`pip install folium`
<br>
`conda install -c pyviz hvplot geoviews`

---

## Usage of Retirement Global+ App

Getting User info:

```python
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
```

Snippet of Monte Carlo code

```python
output = simulation.run_mc_output(df_portfolio, portfolio_type, years_to_retirement)
output
output.calc_cumulative_return()
```

## View of Questionary Stage
![view_questionary](https://user-images.githubusercontent.com/11021924/168452484-30cb0b8b-74b0-4a17-b8da-7570feaa83e8.png)


## Forecast Simulation
![sample_output_MC](https://user-images.githubusercontent.com/11021924/168452488-f5470627-b15b-4166-8dd5-ace160e4e9c0.png)


---

# Useful GitHub commands for Group Coordination

`git checkout -b [BRANCH_NAME]`: new branch

`git checkout [BRANCH_NAME]`: change branch

`git branch` : which branch am I in

when i wanna push code:
<br>
`git add -A` / `git add filename`
<br>
`git commit -m "COMMIT_MESSAGE"`
<br>
`git push`
if this doesn’t work
`git pull --rebase origin master` then try `git push` again

`git branch -D {BRANCH_NAME}` delete branch

---

## Contributors

Tracy Davis
<br>
Reginald Hyppolite
<br>
Jesse Lee
<br>
Wonkyung Lee
<br>
Tyler Shubert

BIG THANKS to all the great TAs and Professor Vinicio DeSola

---

## License
MIT
