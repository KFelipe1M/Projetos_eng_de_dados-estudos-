import requests
import os 
from dotenv import load_dotenv

load_dotenv() #Informações da API key
api_key = os.getenv("API_KEY")

#Interação com a API de Currency
response = requests.get(
     "https://api.freecurrencyapi.com/v1/latest",
    params={
            "apikey": api_key,
            "base_currency": "BRL",
            "currencies": "USD,EUR,JPY"
            }
)

#mostrar o protocolo atual
#de referência;
#200  Sucesso
#400  Erro de cliente
#404  Não encontrado
print(response.status_code)
print(response.json())