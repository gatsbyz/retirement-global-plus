
import get_user_data
import get_cost_of_living_data
import simulation
import fileio

retirement_years, years_to_retirement, savings, portfolio_type, total_stocks_bonds = get_user_data.run()
data, cities = get_cost_of_living_data.cost_of_living_data()
fileio.write_csv([retirement_years, years_to_retirement, savings, portfolio_type, total_stocks_bonds], "cache/user_data.csv")

savings_df = simulation.create_savings_dataframe(savings, total_stocks_bonds)
df_portfolio = simulation.get_portfolio_dataframe()

output = simulation.run_mc_output(df_portfolio, portfolio_type, years_to_retirement)

mean_cumulative_return = simulation.mean_cumulative_return(output, total_stocks_bonds)

savings_at_retirement = simulation.savings_at_retirement(mean_cumulative_return, savings)

retirement_cities = simulation.get_retirement_cities(output, data, retirement_years, total_stocks_bonds, savings)
fileio.write_csv(retirement_cities, "cache/retirement-cities.csv")

print('You can retire in')
print(retirement_cities)