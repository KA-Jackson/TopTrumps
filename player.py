class Player(object):

    def __init__(self, name: str, is_human: bool):
        self.name = name
        self.is_human = is_human
        self.cards = []
        