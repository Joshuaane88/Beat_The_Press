class Player:
    # All possible information that will be used for hints and Guess checks

    def __init__(self, name, club, age, position, league, country, jersey_number,
                 career_goals, career_assists, matches_played, titles_won,
                 clean_sheets=0, yellow_cards=0, red_cards=0,
                 world_cup=False, international_trophy=False):
        self.name = name
        # dictionary to hold core basic player info
        self.reveal_data = {

            "club": club,

            "career_goals": career_goals,

            "career_assists": career_assists,

            "matches_played": matches_played,

            "position": position,

            "age": age,

            "country": country,

            "league": league,

            "titles_won": titles_won,

            "world_cup": world_cup,

            "international_trophy": international_trophy,

            "clean_sheets": clean_sheets,

            "yellow_cards": yellow_cards,

            "red_cards": red_cards


        }


# test case
# if __name__ == "__main__":
#     messi = Player(
#         name="Lionel Messi",
#         club="Inter Miami",
#         age=37,
#         position="Forward",
#         league="MLS",
#         country="Argentina",
#         jersey_number=10,
#         career_goals=838,
#         career_assists=377,
#         matches_played=1069,
#         titles_won=44,
#         world_cup=True
#     )

#     print(f"Player name: {messi.name}")
#     print(f"Reveal data: {messi.reveal_data}")
