import numpy as np

class Game:
    def __init__(self, bc, www, wwl, wpw, wpl, pww, pwl):
        # Payoff schemes:
        self.both_coorporate_utility = bc
        self.WW_winner_utility = www
        self.WW_looser_utility = -wwl
        self.WP_winner_utility = wpw
        self.WP_looser_utility = wpl
        self.PW_winner_utility = pww
        self.PW_looser_utility = pwl


    def evaluate_strategy(self, p1, p2, p1_utility, p2_utility):
        """
        Stochastic evaluation of strategies a and b, where both strategies
        have equal probability (50%) of winning. Where:
        0: defect
        1: coorporate

        :param p1: [0,1] strategy player 1
        :param p2: [0,1] strategy player 2
        :return:
        """

        if(p1_utility or p2_utility):
            prob = p1_utility / (p1_utility + p2_utility)
        else:
            prob = 0.5

        if (p1 == 1 and p2 == 1):  # both coorporate
            return (self.both_coorporate_utility, self.both_coorporate_utility, 1)

        elif (p1 == 1 and p2 == 0):  # p1 coorporate, p2 defect
            if (np.random.rand() < prob):
                return (self.PW_winner_utility, self.PW_looser_utility, 2)
            else:
                return (self.WP_looser_utility, self.WP_winner_utility, 3)

        elif (p1 == 0 and p2 == 1):  # p1 defect, p2 coorporate
            if (np.random.rand() < prob):
                return (self.WP_winner_utility, self.WP_looser_utility, 4)
            else:
                return (self.PW_looser_utility, self.PW_winner_utility, 5)

        elif (p1 == 0 and p2 == 0):  # both defect
            if (np.random.rand() < prob):
                return (self.WW_winner_utility, self.WW_looser_utility, 6)
            else:
                return (self.WW_looser_utility, self.WW_winner_utility, 7)



    def simulate_game(self, p1_strategy, p2_strategy):
        """
        Simulates a two round stochastic game

        :param p1_strategy: [int,int,int,int,int,int,int,int] binary, strategy for player1
        :param p2_strategy: [int,int,int,int,int,int,int,int] binary, strategy for player2

        :return: [int, int] where (player1_payoff, player2_payoff). +1 is winning, -1 is losing, 0 is draw
        """
        p1_utility = 10
        p2_utility = 10

        # first round
        p1_first_strategy = p1_strategy[0]
        p2_first_strategy = p2_strategy[0]
        [p1_reward, p2_reward, state] = self.evaluate_strategy(p1_first_strategy, p2_first_strategy, p1_utility, p2_utility)
        p1_utility += p1_reward
        p2_utility += p2_reward

        # second round
        p1_second_strategy = p1_strategy[state]
        p2_second_strategy = p2_strategy[state]
        [p1_reward, p2_reward, state] = self.evaluate_strategy(p1_second_strategy, p2_second_strategy, p1_utility, p2_utility)
        p1_utility += p1_reward
        p2_utility += p2_reward

        # if(p1_utility > p2_utility):
        #     return [1,0]
        # elif(p1_utility < p2_utility):
        #     return [0,1]
        # else:
        #     return [0,0]
        #
        return(p1_utility-10, p2_utility-10)


