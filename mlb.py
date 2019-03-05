#  http://statsapi-default-elb-prod-876255662.us-east-1.elb.amazonaws.com/api/api_docs

# Standard libraries
from datetime import datetime, timedelta

# Installed libraries
from twisted.internet import task, reactor
import requests

# User-made libraries
from game import Game

def get_games(sport_id, game_type, start_date, end_date):
    """Returns a json array of games.

    Args:
        sport_id (int): integer value of the sport
        game_type (str): single value listed in the GAME_TYPES array
        start_date (date): filter for games
        end_date (date): filter for games

    Returns:
        json: list of games
    """
    url = BASE_URL + '/v1/schedule?sportId=%s&gameType=%s&season=%s&startDate=%s&endDate=%s' % (str(sport_id), game_type, SEASON, start_date.date(), end_date.date())
    response = requests.get(url, headers=HEADER)
    json_data = response.json()
    for date in json_data['dates']:
        for game in date['games']:
            # print(game)
            # game_pk = game['gamePk']
            # live_link = game['link']
            # game_status = game['status']['statusCode']
            # teams = {'home': game['teams']['home']['team']['name'], 'away': game['teams']['away']['team']['name']}
            # score = {'home': game['teams']['home']['score'], 'away': game['teams']['away']['score']}
            # venue = game['venue']['name']
            # content = game['content']['link']
            game_test = Game(game)
            print(game_test.get_score())
    return response.json()
# http://statsapi-default-elb-prod-876255662.us-east-1.elb.amazonaws.com/api/v1/schedule?sportId=1&gameType=R&season=2018&startDate=2018-06-01&endDate=2018-06-02

REFRESH_RATE = 30.0

TODAY = datetime.now() - timedelta(days=1)
# if TODAY.hour > 12:
#     NEXT_DAY = TODAY + timedelta(days=1)
# else:
#     NEXT_DAY = TODAY
#     TODAY = TODAY - timedelta(days=1)
#########################################
# For testing
NEXT_DAY = TODAY
# TODAY = TODAY - timedelta(days=1)
#########################################
BASE_URL = 'http://statsapi-default-elb-prod-876255662.us-east-1.elb.amazonaws.com/api'
HEADER = {'Accept-Encoding': 'gzip'}
SPORT_ID = '1'

# Spring Training, Exhibition, Regular Season, All Star Game, Division Series, First Round (Wild Card), League Championship, World Series
GAME_TYPES = ['S', 'E', 'R', 'A', 'D', 'F', 'L', 'W']
SEASON = TODAY.year

# Get SCHEDULE to pull "Unique Primary Key representing a game"
get_games(1, 'S', TODAY, NEXT_DAY)
exit()
url = BASE_URL + "/v1/schedule?"
response = requests.get(url)
print(response)
print(response.text)

def function_name():
    print('test')
l = task.LoopingCall(function_name)
l.start(REFRESH_RATE)

reactor.run() #ignore linter
