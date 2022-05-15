# Retirement Global +

### Executive Summary

The Retirement Global+ app seeks to flip the script for working citizens around the world. This tool enables users to assess their current assets, as well as their future needs in order to establish an optimized retirement plan to live in any city around the world. The Retirement Global+ app tells you exactly where you can comfortably retire at your preferred retirement age.


### For Users -- General Overview & Flow

Part 1: Data inputs will be generated to determine the years in retirement, size and risk profile of the user's investment portfolio, and historical growth rates of indices.    

Part 2: Users will forecast the performance of their portfolio at the age they wish to retire until the time they choose to retire. Historical price data will be used to generate Monte Carlo simulations to compute total savings (mean) for the time, which elapses btwn the user's current age and the year they prefer to retire.

Part 3: This total cash savings, in addition to asset appreciation will be exported to the Cost of Living Calculator to determine the list of viable cities where the user can retire.

### List of Cities within Scope of Analysis
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
conda install -c pyviz hvplot geoviews

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

### View of Questionary Stage
![view_questioanary](https://github.com/gatsbyz/retirement-global-plus/blob/orion/view_questionary.png)

### Forecast Simulation
![sample_output_MC](https://github.com/gatsbyz/retirement-global-plus/blob/orion/sample_output_MC.png)

---

# Useful GitHub commands for Group Coordination

`git checkout -b [BRANCH_NAME]`: new branch

`git checkout [BRANCH_NAME]`: change branch

`git branch` : where am i

when i wanna push code
`git add -A` / `git add filename`
`git commit -m "COMMIT_MESSAGE"`
`git push`
if this doesn’t work
`git pull --rebase origin master`
then try `git push` again

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

bluesky Retirement Suite 2.0 - patent pending
<br>
Free open.ware for a better world.