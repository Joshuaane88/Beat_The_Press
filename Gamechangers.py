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
        if self.Active["name"] == "False 9":
            pass
        elif self.Active["name"] == "Golden Goal":
            print(r"""
_____/\\\\\\\\\\\\________________/\\\\\\____________/\\\_____________________________________________/\\\\\\\\\\\\_______________________________/\\\\\\____        
 ___/\\\//////////________________\////\\\___________\/\\\___________________________________________/\\\//////////_______________________________\////\\\____       
  __/\\\______________________________\/\\\___________\/\\\__________________________________________/\\\_____________________________________________\/\\\____      
   _\/\\\____/\\\\\\\_____/\\\\\_______\/\\\___________\/\\\______/\\\\\\\\___/\\/\\\\\\_____________\/\\\____/\\\\\\\_____/\\\\\_____/\\\\\\\\\_______\/\\\____     
    _\/\\\___\/////\\\___/\\\///\\\_____\/\\\______/\\\\\\\\\____/\\\/////\\\_\/\\\////\\\____________\/\\\___\/////\\\___/\\\///\\\__\////////\\\______\/\\\____    
     _\/\\\_______\/\\\__/\\\__\//\\\____\/\\\_____/\\\////\\\___/\\\\\\\\\\\__\/\\\__\//\\\___________\/\\\_______\/\\\__/\\\__\//\\\___/\\\\\\\\\\_____\/\\\____   
      _\/\\\_______\/\\\_\//\\\__/\\\_____\/\\\____\/\\\__\/\\\__\//\\///////___\/\\\___\/\\\___________\/\\\_______\/\\\_\//\\\__/\\\___/\\\/////\\\_____\/\\\____  
       _\//\\\\\\\\\\\\/___\///\\\\\/____/\\\\\\\\\_\//\\\\\\\/\\__\//\\\\\\\\\\_\/\\\___\/\\\___________\//\\\\\\\\\\\\/___\///\\\\\/___\//\\\\\\\\/\\__/\\\\\\\\\_ 
        __\////////////_______\/////_____\/////////___\///////\//____\//////////__\///____\///_____________\////////////_______\/////______\////////\//__\/////////__
""")
        elif self.Active["name"] == "Park the Bus":
            pass
        elif self.Active["name"] == "Gegenpress":
            pass
        elif self.Active["name"] == "Transfer Ban":
            pass
        elif self.Active["name"] == "12th Man":
            pass
