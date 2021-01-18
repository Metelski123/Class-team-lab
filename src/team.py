class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def change_coach(self, new_coach):
        self.coach = new_coach

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        found_player = False
        for person in self.players:
            if person == player:
                found_player = True
        return found_player



