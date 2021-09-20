import pandas as pd
from pack import Pack

class CricketPackFactory(object):

    def __load_from_csv(self, file): 

        #Extract cards data into a panda dataframe and limit pack size
        cards_df = pd.read_csv('Data/EnglandTestCricketerData.csv').head(32)

        #Rank cards for each stat -- look to do this programmatically using order
        #cards_df['Runs scored Rank'] = cards_df['Runs scored'].rank(ascending=False)

        #Add cards to pack dictionary
        return cards_df.to_dict(orient='records')

        ##ave to file, converting dictionary to json
        #with open('Data/Pack_EnglandTestCricketersMen.json', 'w') as fileout:
        #    json.dump(pack, fileout)

        return Pack(pack)

    def create_pack(self):

        pack_name = 'England Test Cricketers - Men'
        card_name = 'Name'
        info = ('Playing years', 'Matches played')
        stats = {
            1: {'stat_name': 'Runs scored', 'order': 'High'},
            2: {'stat_name': 'Highest score', 'order': 'High'},
            3: {'stat_name': 'Batting average', 'order': 'High'},
            4: {'stat_name': 'Wickets', 'order': 'High'},
            5: {'stat_name': 'Bowling average', 'order': 'Low'},
            6: {'stat_name': 'Catches', 'order': 'High'}}
        cards = self.__load_from_csv('Data/EnglandTestCricketerData.csv')
    
        pack = Pack(pack_name, card_name, info, stats, cards)
        return pack