"""Game class"""

from datetime import datetime

class Game(object):
    """
    """
    def __init__(self, game):
        self.pk = game['gamePk']
        self.link = game['link']
        self.game_type = game['gameType']
        self.game_date = datetime.fromisoformat(game['gameDate'])
        self.status = game['status']['statusCode']
        self.status_verbose = game['status']['detailedState']
        self.teams = {'home': game['teams']['home']['team'], 'away': game['teams']['away']['team']}
        self.score = {'home': game['teams']['home']['score'], 'away': game['teams']['away']['score']}
        self.venue = game['venue']
        self.content = game['content']

    def get_score(self):
        return {self.teams['home']['name']: self.score['home'], self.teams['away']['name']: self.score['away']}