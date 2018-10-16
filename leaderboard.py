class Leaderboard:
    data = [
        {"username": "Olivia",
         "riddle_status": "Unsolved", 'color': 'purple', 'mystical': 'troll',
         "time_start": "2018/09/16, 20:06:34", "time_stop": '2018/09/16, 20:06:34'},
        {"username": "Alphonso",
         "riddle_status": "Unsolved", 'color': 'blue', 'mystical': 'pumpkin',
         "time_start": "2018/09/12, 20:06:34", "time_stop": '2018/09/12, 20:06:34'},
        {"username": "Carmen",
         "riddle_status": "Unsolved", 'color': 'yellow', 'mystical': 'elephant',
         "time_start": "2018/09/16, 20:06:34", "time_stop": '2018/09/16, 20:06:34'}
    ]

    def __init__(self):
        print("Instance created!")

    def add_player(self, new_player_info):
        self.data.insert(0, new_player_info)

    # def view_players(self):
    #
    #


game_leaderboard = Leaderboard()
