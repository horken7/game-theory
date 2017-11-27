import numpy as np
from .player import Player

class Game:
    def __init__(self, rounds=100):
        # Payoff schemes:
        self.both_coorporate_utility = 2
        self.WW_winner_utility = 4
        self.WW_looser_utility = -1
        self.WP_winner_utility = 2
        self.WP_looser_utility = -1
        self.PW_winner_utility = 4
        self.PW_looser_utility = -2

        self.rounds = rounds
    def evaluate_strategy(self, a, b):
        """
        Stochastic evaluation of strategies a and b, where both strategies
        have equal probability (50%) of winning. Where
        0: defect
        1: coorporate

        :param a: [0,1] strategy a
        :param b: [0,1] strategy b
        :return:
        """
        prob = 0.5

        if (a == 1 and b == 1):  # both coorporate
            return (self.both_coorporate_utility, self.both_coorporate_utility)

        elif (a == 1 and b == 0):  # a coorporate, b defect
            if (np.random.rand() < prob):
                return (self.WP_winner_utility, self.WP_looser_utility)
            else:
                return (self.PW_looser_utility, self.PW_winner_utility)

        elif (a == 0 and b == 1):  # a defect, be coorporate
            if (np.random.rand() < prob):
                return (self.PW_winner_utility, self.PW_looser_utility)
            else:
                return (self.WP_looser_utility, self.WP_winner_utility)

        elif (a == 0 and b == 0):  # both defect
            if (np.random.rand() < prob):
                return (self.WW_winner_utility, self.WW_looser_utility)
            else:
                return (self.WW_looser_utility, self.WW_winner_utility)


    def simulate_2_players(self, p1, p2):
        for i in range(1,self.rounds):
            if(p1.alive() and p2.alive()):
                strategy1 = p1.get_strategy()
                strategy2 = p2.get_strategy()



if __name__ == '__main__':
    rounds = 5000

    game = Game(rounds)

    p1 = Player(0)
    p2 = Player(2)
