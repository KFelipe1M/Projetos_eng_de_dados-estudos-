import requests
import os 
from dotenv import load_dotenv

load_dotenv()

response = requests.get(
     "https://api.freecurrencyapi.com/v1/latest",
    params={
            "api_key": os.getenv("API_KEY"),
            "base_currency": "BRL",
            "currencies": "USD,EUR,JPY"
            }
)

print(response.status_code)
print(response.json())
print(api_key)
print("API_KEY", api_key)