import random as rand


class Game_changer:
    def __init__(self):
        self.Gamechanger_list = [
            {
                "name": "False 9",
                "description": "Revealed hints are fake for the next x seconds",
                "type": "clue",
            },
            {
                "name": "Golden Goal",
                "description": "Next correct guess wins instantly",
                "type": "scoring",
            },
            {
                "name": "Park the Bus",
                "description": "No new hints revealed for the next x seconds",
                "type": "clue",
            },
            {
                "name": "Gegenpress",
                "description": "Guess time reduced, forcing quick decisions",
                "type": "time",
            },
            {
                "name": "Transfer Ban",
                "description": "Players can ban hint categories permanently for the rest of the game",
                "type": "clue",
            },
            {
                "name": "12th Man",
                "description": "Crowd reveals hints in cryptic chant-style clues",
                "type": "clue",
            },
        ]
        self.Active = None

    def Spin_wheel(self):
        selection = rand.choice(self.Gamechanger_list)
        self.Active = selection

    def Reset(self):
        self.Active = None

    def Activate(self):
        if self.active["name"] == "False 9" :
            pass
        if self.active["name"] == "Golden Goal" :
            pass
        if self.active["name"] == "Park the Bus " :
            pass
        if self.active["name"] == "Gegenpress" :
            pass
        if self.active["name"] == "Transfer Ban" :
            pass
        if self.active["name"] == "12th Man" :
            pass