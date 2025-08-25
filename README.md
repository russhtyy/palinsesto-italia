# palinsesto
API per il palinsesto TV italiana: guida completa alla base e all'utilizzo.

## Base API URL
- URL: https://tv-guide-server.herokuapp.com/getChannel/{canale}/{giorno}
- Canale: Per una lista di tutti i canali, scendi giù.
- Giorno: In formato DD-MM-YYYY, esempio: 25-12-2023

## Esempio uso del codice

```python
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
```

## Esempio Risposta
```javascript
[
  {
    "startTime": "00:15",
    "endTime": "00:35",
    "date": "25-12-2023",
    "title": "Pablo",
    "description": null,
    "category": "Cartoni animati",
    "onAir": false,
    "programId": "1535426",
    "withDescription": false
  },
  {
    "startTime": "00:35",
    "endTime": "01:10",
    "date": "25-12-2023",
    "title": "Leo e Tig",
    "description": null,
    "category": "Cartoni animati",
    "onAir": false,
    "programId": "1535427",
    "withDescription": false
  },
  {
    "startTime": "01:10",
    "endTime": "01:15",
    "date": "25-12-2023",
    "title": "Animazione Rai Cinema",
    "description": null,
    "category": "Rubrica",
    "onAir": false,
    "programId": "1535428",
    "withDescription": false
  },
  ...
]
```

## Lista ID & nomi canali TV
```javascript
[
    {"id": "rai_1", "nome": "Rai 1", "canale": "1"},
    {"id": "rai_2", "nome": "Rai 2", "canale": "2"},
    {"id": "rai_3", "nome": "Rai 3", "canale": "3"},
    {"id": "rete4", "nome": "Rete 4", "canale": "4"},
    {"id": "canale5", "nome": "Canale 5", "canale": "5"},
    {"id": "italia_1", "nome": "Italia 1", "canale": "6"},
    {"id": "la7", "nome": "La7", "canale": "7"},
    {"id": "tv8", "nome": "TV8", "canale": "8"},
    {"id": "nove_tv", "nome": "Nove TV", "canale": "9"},
    {"id": "20", "nome": "20", "canale": "20"},
    {"id": "rai_4", "nome": "Rai 4", "canale": "21"},
    {"id": "iris", "nome": "Iris", "canale": "22"},
    {"id": "rai_5", "nome": "Rai 5", "canale": "23"},
    {"id": "raisat_movie", "nome": "Rai Movie", "canale": "24"},
    {"id": "raisat_premium", "nome": "Rai Premium", "canale": "25"},
    {"id": "cielo", "nome": "Cielo", "canale": "26"},
    {"id": "twenty-seven", "nome": "TwentySeven", "canale": "27"},
    {"id": "tv_2000", "nome": "Tv 2000", "canale": "28"},
    {"id": "la7_d", "nome": "La7 D", "canale": "29"},
    {"id": "la5", "nome": "La 5", "canale": "30"},
    {"id": "discovery_real_time", "nome": "Real Time", "canale": "31"},
    {"id": "qvc", "nome": "QVC", "canale": "32"},
    {"id": "food-network", "nome": "Food Network", "canale": "33"},
    {"id": "cine34", "nome": "Cine 34", "canale": "34"},
    {"id": "focus", "nome": "Focus", "canale": "35"},
    {"id": "rtl-102-5", "nome": "RTL 102.5 TV", "canale": "36"},
    {"id": "warner-tv", "nome": "Warner TV", "canale": "37"},
    {"id": "giallo", "nome": "Giallo", "canale": "38"},
    {"id": "top_crime", "nome": "Top Crime", "canale": "39"},
    {"id": "boing", "nome": "Boing", "canale": "40"},
    {"id": "k2", "nome": "K2", "canale": "41"},
    {"id": "rai_gulp", "nome": "Rai Gulp", "canale": "42"},
    {"id": "raisat_yoyo", "nome": "Rai YoYo", "canale": "43"},
    {"id": "frisbee", "nome": "Frisbee", "canale": "44"},
    {"id": "cartoonito", "nome": "Cartoonito", "canale": "46"},
    {"id": "super!", "nome": "Super!", "canale": "47"},
    {"id": "rai_news24", "nome": "Rai News 24", "canale": "48"},
    {"id": "italia2", "nome": "Italia 2", "canale": "49"},
    {"id": "dmax", "nome": "DMAX", "canale": "52"},
    {"id": "rai_storia", "nome": "Rai Storia", "canale": "54"},
    {"id": "mediaset_extra", "nome": "Mediaset Extra", "canale": "55"},
    {"id": "hgtv", "nome": "HGTV", "canale": "56"},
    {"id": "rai-scuola", "nome": "Rai Scuola", "canale": "57"},
    {"id": "raisport_hd", "nome": "Rai Sport", "canale": "58"},
    {"id": "motor-trend", "nome": "Motor Trend", "canale": "59"},
    {"id": "sportitalia", "nome": "Sportitalia", "canale": "60"},
    {"id": "supertennis", "nome": "SuperTennis", "canale": "64"},
    {"id": "alma_tv", "nome": "ALMA TV", "canale": "65"},
    {"id": "vh1", "nome": "VH1", "canale": "167"},
    {"id": "sky_uno", "nome": "Sky Uno", "canale": "108"},
    {"id": "sky_atlantic", "nome": "Sky Atlantic", "canale": "110"},
    {"id": "sky_serie", "nome": "Sky Serie", "canale": "112"},
    {"id": "sky_investigation", "nome": "Sky Investigation", "canale": "114"},
    {"id": "sky-arte", "nome": "Sky Arte", "canale": "120"},
    {"id": "comedy_central", "nome": "Comedy Central", "canale": "129"},
    {"id": "mtv", "nome": "MTV", "canale": "131"},
    {"id": "mtv-music", "nome": "MTV Music", "canale": "132"},
    {"id": "gambero-rosso", "nome": "Gambero Rosso", "canale": "133"},
    {"id": "class_tv_moda", "nome": "Class TV Moda", "canale": "180"},
    {"id": "sky_sport_24", "nome": "Sky Sport 24", "canale": "200"},
    {"id": "sky_sport_uno", "nome": "Sky Sport Uno", "canale": "201"},
    {"id": "sky-sport-calcio", "nome": "Sky Sport Calcio", "canale": "202"},
    {"id": "sky-sport-tennis", "nome": "Sky Sport Tennis", "canale": "203"},
    {"id": "sky_sport_arena", "nome": "Sky Sport Arena", "canale": "204"},
    {"id": "sky-sport-action", "nome": "Sky Sport Action", "canale": "205"},
    {"id": "sky-sport-f1", "nome": "Sky Sport F1", "canale": "207"},
    {"id": "sky-sport-motogp", "nome": "Sky Sport MotoGP", "canale": "208"},
    {"id": "sky-sport-nba", "nome": "Sky Sport NBA", "canale": "209"},
    {"id": "eurosport_hd", "nome": "Eurosport", "canale": "210"},
    {"id": "eurosport_2", "nome": "Eurosport 2", "canale": "211"},
    {"id": "horse_tv", "nome": "Horse TV", "canale": "221"},
    {"id": "sky_cinema_uno", "nome": "Sky Cinema Uno", "canale": "301"},
    {"id": "sky_cinema_due", "nome": "Sky Cinema Due", "canale": "302"},
    {"id": "sky_cinema_collection", "nome": "Sky Cinema Collection", "canale": "303"},
    {"id": "sky_cinema_family_hd", "nome": "Sky Cinema Family", "canale": "304"},
    {"id": "sky_cinema_action", "nome": "Sky Cinema Action", "canale": "305"},
    {"id": "sky_cinema_suspence", "nome": "Sky Cinema Suspence", "canale": "306"},
    {"id": "sky_cinema_romance", "nome": "Sky Cinema Romance", "canale": "307"},
    {"id": "sky_cinema_drama", "nome": "Sky Cinema Drama", "canale": "308"},
    {"id": "sky_cinema_comedy", "nome": "Sky Cinema Comedy", "canale": "309"},
    {"id": "sky-documentaries", "nome": "Sky Documentaries", "canale": "402"},
    {"id": "sky-nature", "nome": "Sky Nature", "canale": "404"},
    {"id": "discovery_channel_hd", "nome": "Discovery Channel", "canale": "405"},
    {"id": "history_channel", "nome": "History", "canale": "411"},
    {"id": "ci-crime-investigation", "nome": "Crime + Investigation", "canale": "414"},
    {"id": "class_cnbc", "nome": "Class CNBC", "canale": "507"},
    {"id": "nickelodeon", "nome": "Nickelodeon", "canale": "605"},
    {"id": "cartoon_network", "nome": "Cartoon Network", "canale": "607"},
    {"id": "boomerang", "nome": "Boomerang", "canale": "609"}
]
```
