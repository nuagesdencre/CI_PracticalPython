class Leaderboard:
    def __init__(self):
        self.data = [
            {"username": "Luis",
             "riddle_status": "Unsolved", 'color': 'pink', 'mystical': 'emu',
             "time_start": "12/09/2018, 10:02:34", "time_stop": '12/09/2018, 11:06:22'},
            {"username": "Olivia",
             "riddle_status": "Solved", 'color': 'purple', 'mystical': 'troll',
             "time_start": "16/09/2018, 20:06:31", "time_stop": '16/09/2018, 20:06:14'},
            {"username": "Alphonso",
             "riddle_status": "Unsolved", 'color': 'blue', 'mystical': 'pumpkin',
             "time_start": "22/09/2018, 20:06:38", "time_stop": '22/09/2018, 20:06:36'}
        ]

# adds current visitor's inputted details to data
    def add_player(self, new_player_info):
        self.data.insert(0, new_player_info)

# selects first 3 dictionaries as per the data list index
    def get_leaders(self):
        leaders = self.data[:3]
        return leaders
