import numpy as np
import matplotlib.pyplot as plt
import copy
from itertools import product

from player import Player
from game import Game


class Evolution:
    def __init__(self, number_of_players, rounds, bc, www, wwl, wpw, wpl, pww, pwl):
        self.players = {}
        self.alive = []

        self.nr_players = number_of_players

        self.game = Game(bc, www, wwl, wpw, wpl, pww, pwl)

        self.rounds = rounds


    def init_players_randomly(self):
        for i in range(self.nr_players):
            strategy = np.random.choice([0,1], size=(8,))
            decimal = int("".join(map(str, strategy)), 2)
            player = Player(strategy, self.rounds)
            self.players[decimal] = player
        self.alive = list(self.players.keys())


    def init_all_players(self):
        n = 8 # nr of different choises in the game tree
        strategies = [list(i) for i in product([0, 1], repeat=n)] # all binary 9 bit combinations
        for s in strategies:
            player = Player(s, self.rounds)
            decimal = int("".join(map(str, s)), 2)
            self.players[decimal] = player
        self.alive = list(self.players.keys())

    def simulate_game(self, p1, p2, t):
        p1_strategy = p1.get_strategy()
        p2_strategy = p2.get_strategy()

        [p1_utility, p2_utility] = self.game.simulate_game(p1_strategy, p2_strategy)
        p1.update_score(t, p1_utility)
        p2.update_score(t, p2_utility)


    def simulate_evolution(self):
        for t in range(1, self.rounds):
            for ind, p1 in enumerate(self.alive):
                player_1 = self.players[p1]
                for p2 in self.alive[ind:]:
                    player_2 = self.players[p2]
                    self.simulate_game(player_1, player_2, t)

            sum_points = 0
            for p in self.alive:
                sum_player = self.players[p].utility[t]
                sum_points += sum_player
            for p in copy.deepcopy(self.alive):
                sum_player = self.players[p].utility[t]
                part_player = sum_player/sum_points
                if(part_player < 0.0025):
                    self.alive.remove(p)
        print(t)



    def plot_stuff(self):
        plt.title('Two Round Prisoners Evolution')
        ax = plt.subplot(1, 1, 1)
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Utility')
        for key, player in self.players.items():
            ax.plot(np.linspace(1, len(player.utility[1:]), len(player.utility[1:])), player.utility[1:],
                    label=str(player.strategy))
        # handles, labels = ax.get_legend_handles_labels()
        # ax.legend(handles, labels)

        plt.show()
