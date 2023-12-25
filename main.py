import requests
from datetime import datetime

canale = "raisat_yoyo"
giorno = datetime.today().strftime('%d-%m-%Y')

url = f'https://tv-guide-server.herokuapp.com/getChannel/{canale}/{giorno}'
headers = {
    'Host': 'tv-guide-server.herokuapp.com',
    'Connection': 'keep-alive',
    'appVersionCode': '3',
    'Operating-System': 'iOS',
    'Accept': '*/*',
    'Accept-Language': 'en-ca',
    'token': '6c012c88b464bcec9e4fcf84304b8949',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'GuidaTv/3 CFNetwork/1220.1 Darwin/20.3.0'
}

response = requests.get(url, headers=headers)
print(response.json())
