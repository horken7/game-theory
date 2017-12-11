import numpy as np
import matplotlib.pyplot as plt
import copy
from itertools import product

from player import Player
from game import Game


class Evolution:
    def __init__(self, number_of_players, rounds, bc, www, wwl, wpw, wpl, pww, pwl):
        self.players = []
        self.nr_players = number_of_players

        self.game = Game(bc, www, wwl, wpw, wpl, pww, pwl)

        self.rounds = rounds


    def init_players_randomly(self):
        for i in range(self.nr_players):
            strategy = np.random.choice([0,1], size=(8,))
            player = Player(strategy, self.rounds)
            self.players.append(player)
        self.players[0].strategy = [0,0,0,0,0,0,0,0]
        self.players[1].strategy = [1,1,1,1,1,1,1,1]


    def simulate_game(self, p1, p2, t):
        p1_strategy = p1.get_strategy()
        p2_strategy = p2.get_strategy()

        [p1_utility, p2_utility] = self.game.simulate_game(p1_strategy, p2_strategy)
        p1.update_score(t, p1_utility)
        p2.update_score(t, p2_utility)


    def simulate_evolution(self):
        for t in range(1, self.rounds):
            tmp_players = copy.deepcopy(self.players)
            for player_1 in self.players:
                for player_2 in tmp_players:
                    self.simulate_game(player_1, player_2, t)
                del tmp_players[0]





    def plot_average_and_accumulated(self):
        plt.title('Two Round Prisoners Evolution')
        ax = plt.subplot(1, 1, 1)
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Accumulated Utility')
        for player in self.players:
            ax.plot(np.linspace(1, len(player.accumulated_utility), len(player.accumulated_utility)), player.accumulated_utility,
                    label=str(player.strategy))
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)

        plt.show()

        # p1 = self.players[0]
        # p2 = self.players[1]
        #
        # plt.suptitle('Two Round Prisoners Evolution')
        # ax = plt.subplot(1, 2, 1)
        # ax.plot(np.linspace(1, len(p1.average_utility), len(p1.average_utility)), p1.average_utility,
        #         label=str(p1.strategy))
        # ax.plot(np.linspace(1, len(p2.average_utility), len(p2.average_utility)), p2.average_utility,
        #         label=str(p2.strategy))
        # ax.set_xlabel('Iterations')
        # ax.set_ylabel('Average Utility')
        # handles, labels = ax.get_legend_handles_labels()
        # ax.legend(handles, labels)
        #
        # ax = plt.subplot(1, 2, 2)
        # ax.plot(np.linspace(1, len(p1.accumulated_utility), len(p1.accumulated_utility)), p1.accumulated_utility,
        #         label=str(p1.strategy))
        # ax.plot(np.linspace(1, len(p2.accumulated_utility), len(p2.accumulated_utility)), p2.accumulated_utility,
        #         label=str(p2.strategy))
        # ax.set_xlabel('Iterations')
        # ax.set_ylabel('Accumulated utility')
        # handles, labels = ax.get_legend_handles_labels()
        # ax.legend(handles, labels)
        # plt.show()