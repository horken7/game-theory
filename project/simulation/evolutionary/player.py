import numpy as np

class Player:

    def __init__(self, strategy=[0,0,0,0,0,0,0,0], rounds=10):
        """

        :param strategy:
        :param rounds:

        """

        self.utility = np.zeros(rounds)
        self.abundance = np.zeros(rounds)

        self.strategy = strategy

    def update_score(self, t, score):
        self.utility[t] += score

    def update_abundance(self, t, abundance):
        self.abundance[t] = abundance

    def get_strategy(self):
        return self.strategy