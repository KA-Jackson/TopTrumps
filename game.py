from pack import Pack
from player import Player
import pack_selector
import random

def get_first_chooser(players: list):
    return players[random.randint(1, len(players)) - 1]

def get_players_cards_for_hand(players):
    player_cards = {}
    for player in players:
        if player.cards:
            player_cards[player] = player.cards.pop()
    return player_cards

def get_hand_winner(player_cards: dict, stat: dict) -> dict:
    card_compare = {}
    for k, v in player_cards.items():
        card_compare[k] = v[stat['stat_name']]
    if stat['order'] == 'Low':
        return min(card_compare, key=card_compare.get)
    else:
        return max(card_compare, key=card_compare.get)

def show_choosers_card(card: dict, pack: Pack) -> str:
    card_str = pack.card_name + ': ' + card[pack.card_name] + '\n'
    for l in pack.info:
        card_str += str(l) + ': ' + str(card[l]) + '\n'
    for k, v in pack.stats.items():
        card_str += '(' + str(k) + ') ' + v['stat_name'].ljust(pack.max_len_stat) + '\t' + str(card[v['stat_name']]) + '\n'
    return card_str
    
def select_stat(chooser: Player, stats: list):

    if chooser.is_human == 1:
        selected_stat_id = input(chooser.name + ', select your stat (1-' + str(len(stats)) + ')')
    else:
        selected_stat_id = random.randint(1, len(stats))
    try:
        stat = stats[int(selected_stat_id)]
    except:
        stat = select_stat(chooser, stats)
    return stat

def play_hand(chooser: Player, players: list, pack: Pack):
    print(chooser.name, 'to select the stat')
    player_cards = get_players_cards_for_hand(players)
    print(show_choosers_card(player_cards[chooser], pack))
    stat = select_stat(chooser, pack.stats)
    print(chooser.name, 'chose:', stat['stat_name'])
    for player in players:
        if player not in player_cards:
            print(player.name, 'is OUT')
        else:
            print(player.name, '-', player_cards[player][pack.card_name], ':', player_cards[player][stat['stat_name']])
    winner = get_hand_winner(player_cards, stat)
    print('***', winner.name.upper(), 'wins the hand! ***')
    for k, v in player_cards.items():
        winner.cards.insert(0, v)
    print('-'*3, 'Player card counts:')
    for player in players:
            print(player.name, len(player.cards))
    return winner

def check_game_winner(round_number: int, players: list, player_placings: dict) -> bool:
    players_with_cards = 0
    for player in players:
        if player.cards:
            players_with_cards += 1
        else:
            if player not in player_placings.keys():
                player_placings[player] = round_number
    return players_with_cards == 1 

def show_final_placings(winner: Player, player_placings: dict):
    print(winner.name, "IS THE WINNER!!!")
    sort_placings = sorted(player_placings.items(), key=lambda player: player[1], reverse=True)
    for player in sort_placings:
        print(player[0].name, 'was out in hand:', player[1])

def play_game():
    players = [
        Player('Kevin', 1),
        Player('George', 0),
        Player('Rachael', 0),
        Player('Daisy', 0)]

    pack = pack_selector.get_pack('cricket')
    pack.shuffle()
    pack.deal(players)
    chooser = get_first_chooser(players)
    game_won = False
    player_placings = {}
    round_number = 0

    while not game_won:
        round_number += 1
        print('-' * 10, 'HAND', round_number, '-' * 10)
        chooser = play_hand(chooser, players, pack)
        game_won = check_game_winner(round_number, players, player_placings)
    show_final_placings(chooser, player_placings)  

play_game()