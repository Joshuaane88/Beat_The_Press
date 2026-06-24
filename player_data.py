from shell import Player


def load_players():
    players = [

        Player(
            name="Alisson Becker",
            club="Liverpool",
            age=33,
            position="Goalkeeper",
            league="Premier League",
            country="Brazil",
            jersey_number=13,
            career_goals=1,
            career_assists=3,
            matches_played=450,
            titles_won=13,
            world_cup=False,
            international_trophy=True,
            clean_sheets=220,
            yellow_cards=5,
            red_cards=0),

        Player(
            name="Virgil van Dijk",
            club="Liverpool",
            age=34,
            position="Defender",
            league="Premier League",
            country="Netherlands",
            jersey_number=4,
            career_goals=60,
            career_assists=18,
            matches_played=634,
            titles_won=11,
            world_cup=False,
            international_trophy=True,
            clean_sheets=180,
            yellow_cards=50,
            red_cards=3
        ),


        Player(
            name="Jude Bellingham",
            club="Real Madrid",
            age=22,
            position="Midfielder",
            league="La Liga",
            country="England",
            jersey_number=5,
            career_goals=54,
            career_assists=26,
            matches_played=236,
            titles_won=4,
            world_cup=False,
            international_trophy=False,
            clean_sheets=0,
            yellow_cards=20,
            red_cards=2
        ),


        Player(
            name="Kevin De Bruyne",
            club="Napoli",
            age=34,
            position="Midfielder",
            league="Serie A",
            country="Belgium",
            jersey_number=11,
            career_goals=108,
            career_assists=265,
            matches_played=574,
            titles_won=18,
            world_cup=False,
            international_trophy=False,
            clean_sheets=0,
            yellow_cards=40,
            red_cards=1
        ),


        Player(
            name="Vinicius Jr",
            club="Real Madrid",
            age=25,
            position="Forward",
            league="La Liga",
            country="Brazil",
            jersey_number=7,
            career_goals=106,
            career_assists=82,
            matches_played=322,
            titles_won=14,
            world_cup=False,
            international_trophy=False,
            clean_sheets=0,
            yellow_cards=35,
            red_cards=3
        ),


        Player(
            name="Robert Lewandowski",
            club="Barcelona",
            age=37,
            position="Forward",
            league="La Liga",
            country="Poland",
            jersey_number=9,
            career_goals=700,
            career_assists=193,
            matches_played=892,
            titles_won=31,
            world_cup=False,
            international_trophy=False,
            clean_sheets=0,
            yellow_cards=25,
            red_cards=2
        ),


        Player(
            name="Mohamed Salah",
            club="Liverpool",
            age=33,
            position="Forward",
            league="Premier League",
            country="Egypt",
            jersey_number=11,
            career_goals=329,
            career_assists=146,
            matches_played=648,
            titles_won=14,
            world_cup=False,
            international_trophy=False,
            clean_sheets=0,
            yellow_cards=30,
            red_cards=1),


        Player(
            name="Erling Haaland",
            club="Manchester City",
            age=25,
            position="Forward",
            league="Premier League",
            country="Norway",
            jersey_number=9,
            career_goals=300,
            career_assists=55,
            matches_played=354,
            titles_won=15,
            world_cup=False,
            international_trophy=False,
            clean_sheets=0,
            yellow_cards=10,
            red_cards=0),


        Player(
            name="Kylian Mbappé",
            club="Real Madrid",
            age=26,
            position="Forward",
            league="La Liga",
            country="France",
            jersey_number=10,
            career_goals=350,
            career_assists=170,
            matches_played=410,
            titles_won=15,
            world_cup=True,
            international_trophy=True,
            clean_sheets=0,
            yellow_cards=15,
            red_cards=1),

        Player(
            name="Lionel Messi",
            club="Inter Miami",
            age=37,
            position="Forward",
            league="MLS",
            country="Argentina",
            jersey_number=10,
            career_goals=838,
            career_assists=377,
            matches_played=1069,
            titles_won=44,
            world_cup=True,
            international_trophy=True,
            clean_sheets=0,
            yellow_cards=32,
            red_cards=3
        ),

        Player(
            name="Mohammed Kudus",
            club="Tottenham Hotspur",
            age=25,
            position="Midfielder",
            league="Premier League",
            country="Ghana",
            jersey_number=20,
            career_goals=60,
            career_assists=25,
            matches_played=225,
            titles_won=3,
            world_cup=False,
            international_trophy=False,
            clean_sheets=0,
            yellow_cards=18,
            red_cards=1),
    ]

    return players

# test code


if __name__ == "__main__":
    all_players = load_players()
    print(f"Loaded {len(all_players)} players:")
    for player in all_players:
        print(
            f"  - {player.name} ({player.reveal_data['position']}) - {player.reveal_data['club']}")
