from datetime import datetime

import requests

TODAY = datetime.now()
BASE_URL = 'http://statsapi-default-elb-prod-876255662.us-east-1.elb.amazonaws.com/api'
HEADER = {'Accept-Encoding': 'gzip'}
SPORT_ID = '1'

# Spring Training, Exhibition, Regular Season, All Star Game, Division Series, First Round (Wild Card), League Championship, World Series
GAME_TYPES = ['S', 'E', 'R', 'A', 'D', 'F', 'L', 'W']
SEASON = int(TODAY.year) - 1

# Get SCHEDULE to pull "Unique Primary Key representing a game"
url = BASE_URL + "/v1/schedule?"
response = requests.get(url)
print(response)
print(response.text)


def get_today_games(gameType):
    pass
# http://statsapi-default-elb-prod-876255662.us-east-1.elb.amazonaws.com/api/v1/schedule?sportId=1&gameType=R&season=2018&startDate=2018-06-01&endDate=2018-06-02