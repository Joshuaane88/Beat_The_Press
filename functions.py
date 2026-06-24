from player_data import load_players
all_players = load_players()


def eliminate(stat, value, lst=all_players):
    eliminated_list = []
    for player in lst:
        try:
            check = player.reveal_data[stat]
        except KeyError:
            err = "Key not found, using default."
            return err
        if check == value:
            eliminated_list.append(player)
    return eliminated_list
