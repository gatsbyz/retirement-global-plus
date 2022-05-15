# Retirement Global +

# Google Docs
https://docs.google.com/document/d/1laAHUYkqxnocPBQqIeRB0HaU6wA8JShfNR4nlD4YaIU/edit?usp=sharing
https://docs.google.com/document/d/1g50-IH0gQW8BT-l-CZcedZe2tRH1bg2ENcP3v_ge1W0/edit?usp=sharing

# useful git commands
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

# how to run
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

# sample input
? What is your current age 25

? By what age, would you prefer to retire? 65

? How much do you have in liquid cash savings (USD) 50000

? Would you like your portfolio to be conservative[1], conservatively moderate[2], or moderate[3]? 3


? How much would you like to invest in stocks and bonds? 40000

# sample output 
You can retire in
['Paris/France', 'Hamilton/Canada', 'Milan/Italy', 'Bucaramanga/Colombia', 'Madrid/Spain', 'Delhi/India']
