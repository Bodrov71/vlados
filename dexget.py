import requests


platform_bsc = 'eth-ethereum'
base_contract = '0x64bc2ca1be492be7185faa2c8835d9b824c8a194'



def get_token_info_m():
    url = "https://api.coinpaprika.com/v1/contracts/" + platform_bsc + "/" + base_contract
    headers = {
        "X-RapidAPI-Key": "2652a67c6dmsh3e1551f3c1d6e4ap177be3jsna39fae9531be",
        "X-RapidAPI-Host": "coinpaprika1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers) #params=params)
    print(response.json())

get_token_info_m()