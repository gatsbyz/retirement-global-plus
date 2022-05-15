import os
from dotenv import load_dotenv
import json
import requests

# Load the environment variables from the .env file by calling the load_dotenv function
load_dotenv()

COST_OF_LIVING_URL = os.getenv("COST_OF_LIVING_URL")
COST_OF_LIVING_HEADERS = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": os.getenv("RAPID_API_HOST"),
	"X-RapidAPI-Key":  os.getenv("RAPID_API_KEY")
}

payload = {
  'cities': '[{"name":"Hamilton","country":"Bermuda"},{"name":"New York","country":"United States"},{"name":"Hong Kong","country":"Hong Kong"},{"name":"Los Angeles","country":"United States"},{"name":"Paris","country":"France"},{"name":"Hamilton","country":"Canada"},{"name":"Milan","country":"Italy"},{"name":"Bucaramanga","country":"Colombia"},{"name":"Madrid","country":"Spain"},{"name":"Delhi","country":"India"}]',
  'currencies': '["USD"]'
}

def cost_of_living_data():
    #########################
    ### real fetch to API ###
    #########################
	response = requests.request("POST", COST_OF_LIVING_URL, data=payload, headers=COST_OF_LIVING_HEADERS)
	rawData = response.json()['data']
	# print(rawData)

    #########################
    ## test data from json ##
    #########################
	# f = open('static/test-data.json')
	# rawData = json.load(f)
	# f.close()

	data = []
	cities = []

	for item in rawData:
		cities.append(item['name'])

		cityData = {}
		cityData['city'] = item['name']
		cityData['country'] = item['country']
		cityData['rent_index'] = float(item['rent_index'])
		cityData['restaurant_price_index'] = float(item['restaurant_price_index'])
		cityData['groceries_index'] = float(item['groceries_index'])
		cityData['cost_of_living_index'] = float(item['cost_of_living_index'])
		cityData['cost_of_living_plus_rent_index'] = float(item['cost_of_living_plus_rent_index'])
		cityData['local_purchasing_power_index'] = float(item['local_purchasing_power_index'])

		cost_of_living = item['cost_of_living_details'][0]['details']
		estimated_cost_without_rent = next(x for x in cost_of_living if x['Item'] == "Estimated Monthly Costs Without Rent")
		rent = next(x for x in cost_of_living if x['Item'] == "Apartment (1 bedroom) Outside of Centre")

		cityData['estimated_monthly_costs_with_rent'] = float(estimated_cost_without_rent['Value']) + float(rent['Value'])
		cityData['estimated_monthly_costs_without_rent'] = float(estimated_cost_without_rent['Value'])

		data.append(cityData)


	# print(json.dumps(data, indent=4, sort_keys=True))
	# print(cities)

	return data, cities