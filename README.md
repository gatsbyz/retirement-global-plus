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
1. Run `python3 main.py` in terminal to start calculator.
2. Enter your retirement information.
3. Your input will be saved in `user_data.csv`
4. The CLI will show you the cities you can retire in.
5. Your retirement cities will be saved in `retirement-cities.csv`
6. run `retirement_tool.ipynb` to visualize your retirement data. the most recent user input will be used.
7. run `map_retirement_cities.ipynb` to visualize your retirement cities. the most recent retirement cities will be used.
8. retire