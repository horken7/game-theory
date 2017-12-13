import numpy as np
import  matplotlib.pyplot as plt


class Game:
    def __init__(self, rounds, bc, www, wwl, wpw, wpl, pww, pwl):
        # Payoff schemes:
        self.both_coorporate_utility = bc
        self.WW_winner_utility = www
        self.WW_looser_utility = -wwl
        self.WP_winner_utility = wpw
        self.WP_looser_utility = wpl
        self.PW_winner_utility = pww
        self.PW_looser_utility = pwl

        self.rounds = rounds

    def evaluate_strategy(self, p1, p2):
        """
        Stochastic evaluation of strategies a and b, where both strategies
        have equal probability (50%) of winning. Where:
        0: defect
        1: coorporate

        :param a: [0,1] strategy a
        :param b: [0,1] strategy b
        :return:
        """
        prob = 0.5

        if (p1 == 1 and p2 == 1):  # both coorporate
            return (self.both_coorporate_utility, self.both_coorporate_utility)

        elif (p1 == 1 and p2 == 0):  # p1 coorporate, p2 defect
            if (np.random.rand() < prob):
                return (self.WP_winner_utility, self.WP_looser_utility)
            else:
                return (self.PW_looser_utility, self.PW_winner_utility)

        elif (p1 == 0 and p2 == 1):  # p1 defect, p2 coorporate
            if (np.random.rand() < prob):
                return (self.PW_winner_utility, self.PW_looser_utility)
            else:
                return (self.WP_looser_utility, self.WP_winner_utility)

        elif (p1 == 0 and p2 == 0):  # both defect
            if (np.random.rand() < prob):
                return (self.WW_winner_utility, self.WW_looser_utility)
            else:
                return (self.WW_looser_utility, self.WW_winner_utility)


    def evaluate_relative_stochastic_strategy(self, p1, p2, player1, player2):
        """
        Stochastic evaluation of strategies a and b, where both strategies
        have equal probability (50%) of winning. Where:
        0: defect
        1: coorporate

        :param a: [0,1] strategy a
        :param b: [0,1] strategy b
        :return:
        """
        prob = player1.accumulated_resources[-1] / (player1.accumulated_resources[-1] + player2.accumulated_resources[-1])

        if (p1 == 1 and p2 == 1):  # both coorporate
            return (self.both_coorporate_utility, self.both_coorporate_utility)

        elif (p1 == 1 and p2 == 0):  # p1 coorporate, p2 defect
            if (np.random.rand() < prob):
                return (self.WP_winner_utility, self.WP_looser_utility)
            else:
                return (self.PW_looser_utility, self.PW_winner_utility)

        elif (p1 == 0 and p2 == 1):  # p1 defect, p2 coorporate
            if (np.random.rand() < prob):
                return (self.PW_winner_utility, self.PW_looser_utility)
            else:
                return (self.WP_looser_utility, self.WP_winner_utility)

        elif (p1 == 0 and p2 == 0):  # both defect
            if (np.random.rand() < prob):
                return (self.WW_winner_utility, self.WW_looser_utility)
            else:
                return (self.WW_looser_utility, self.WW_winner_utility)


    def simulate_2_players(self, p1, p2):
        for t in range(1,self.rounds):
            if(p1.alive() and p2.alive()):
                strategy1 = p1.get_strategy(p1.actions, p2.actions, t)
                strategy2 = p2.get_strategy(p2.actions, p1.actions, t)
                [utility1, utility2] = self.evaluate_strategy(strategy1, strategy2)
                # [utility1, utility2] = self.evaluate_relative_stochastic_strategy(strategy1, strategy2, p1, p2)
                p1.update_history(utility1, strategy1, t)
                p2.update_history(utility2, strategy2, t)

    def plot_average_and_accumulated(self, p1, p2):
        plt.suptitle('Iterated Prisoners')
        ax = plt.subplot(1, 2, 1)
        ax.plot(np.linspace(1, len(p1.average_utility), len(p1.average_utility)), p1.average_utility,
                label=p1.strategy_name)
        ax.plot(np.linspace(1, len(p2.average_utility), len(p2.average_utility)), p2.average_utility,
                label=p2.strategy_name)
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Average Utility')
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)

        ax = plt.subplot(1, 2, 2)
        ax.plot(np.linspace(1, len(p1.accumulated_resources), len(p1.accumulated_resources)), p1.accumulated_resources,
                label=p1.strategy_name)
        ax.plot(np.linspace(1, len(p2.accumulated_resources), len(p2.accumulated_resources)), p2.accumulated_resources,
                label=p2.strategy_name)
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Accumulated utility')
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)
        plt.show()
