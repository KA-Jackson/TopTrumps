from pack import Pack
from player import Player
import pack_selector
import random

def get_cards_for_hand(players):
    player_cards = {}
    for player in players:
        if len(player.cards) > 0:
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
    selected_stat_id = input(chooser.name + ', select your stat (1-' + str(len(stats)) + ')')
    try:
        stat = stats[int(selected_stat_id)]
    except:
        stat = select_stat(chooser, stats)
    return stat

def play_hand(chooser: Player, players: list, pack: Pack):

    player_cards = get_cards_for_hand(players)
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
    return winner

def play_game():
    players = [
        Player('Kevin'),
        Player('George'),
        Player('Rachael'),
        Player('Daisy')]

    pack = pack_selector.get_pack('cricket')
    pack.shuffle()
    pack.deal(players)

    chooser = players[random.randint(1, len(players)) - 1]

    for i in range(1, 101):
        print('----------', 'ROUND', i, '----------')
        chooser = play_hand(chooser, players, pack)
        for player in players:
            print(player.name, len(player.cards))

play_game()