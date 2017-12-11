import numpy as np

class Player:

    def __init__(self, strategy=[0,0,0,0,0,0,0,0], rounds=10):
        """

        :param strategy:
        :param rounds:

        """

        self.round_score = 0

        self.accumulated_utility = np.zeros(rounds)

        self.strategy = strategy


    def update_score(self, t, score):
        self.accumulated_utility[t] += score

    def get_strategy(self):
        return self.strategy
