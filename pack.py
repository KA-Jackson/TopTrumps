import random
import pandas as pd

class Pack(object):

    def __add_stat_ranks(self):
        cards_df = pd.DataFrame.from_dict(self.cards)
        for stat in self.stats.values():
            ascend = stat['order'] == 'Low'
            cards_df[stat['stat_name'] + ' Rank'] = cards_df[stat['stat_name']].rank(ascending=ascend).astype(int)
            #cards_df['Runs scored Rank'] = cards_df['Runs scored'].rank(ascending=ascend).astype(int)
        self.cards = cards_df.to_dict(orient='records')

    def __init__(self, pack_name: str, card_name: str, info, stats, cards):
        self.pack_name = pack_name
        self.card_name = card_name
        self.info = info
        self.stats = stats
        self.cards = cards
        max_len = 0
        for v in stats.values():
            max_len = max(max_len, len(v['stat_name']))
        self.max_len_stat = max_len
        self.__add_stat_ranks()

    def __deal_round(self, players, deal_cards):
        for player in players:
            if len(deal_cards) > 0:
                player.cards.append(deal_cards.pop())

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, players):
        deal_cards = self.cards.copy()
        while len(deal_cards) > 0:
            self.__deal_round(players, deal_cards)