import random as rand


class AI_base:

    def __init__(self, list_of_Players, difficulty=None):
        self.list_of_Players = list_of_Players
        self.difficulty = difficulty
        self.clues = {}
        self.candidates = list(list_of_Players)

    def receive_hints(self, hints):
        self.clues.update(hints)

        guess_list = []
        for player in self.candidates:
            match = True
            for stat, value in self.clues.items():
                check = player.reveal_data[stat]
                if check != value:
                    match = False
            if match:
                guess_list.append(player)
        self.candidates = guess_list

    def make_guess(self):
        difficulty_check = self.difficulty
        obvious_clues = ["position", "league", "country", "club"]

        if difficulty_check == "Easy":
            easy_guess = rand.choice(self.candidates)
            easy_guess = easy_guess.name
            return easy_guess

        elif difficulty_check == "Medium":
            medium_guess_list = []

            for player in self.candidates:
                match = True
                for stat, value in self.clues.items():
                    if stat in obvious_clues:
                        check = player.reveal_data[stat]
                        if check != value:
                            match = False
                if match:
                    medium_guess_list.append(player)

            medium_guess = rand.choice(medium_guess_list)
            medium_guess = medium_guess.name
            return medium_guess

        elif difficulty_check == "Hard":
            confidence_lvl = 1 - (len(self.candidates) / len (self.list_of_Players))
            if confidence_lvl > 0.7 and len(self.candidates) < 5 :
                hard_choice = rand.choice(self.candidates)
                hard_choice = hard_choice.name
                return hard_choice
            else:
                
                


        elif difficulty_check == "Super":
            pass
