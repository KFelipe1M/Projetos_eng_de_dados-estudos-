import requests
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

response = requests.get(
     "https://api.freecurrencyapi.com/v1/latest",
    params={
            "apikey": api_key,
            "base_currency": "BRL",
            "currencies": "USD,EUR,JPY"
            }
)

print(response.status_code)
print(response.json())