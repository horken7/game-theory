import numpy as np
import matplotlib.pyplot as plt
import copy
from itertools import product

from player import Player
from game import Game


class Evolution:
    def __init__(self, rounds, bc, www, wwl, wpw, wpl, pww, pwl):
        self.population_size = 5000  # for replicator dynamics

        self.game = Game(bc, www, wwl, wpw, wpl, pww, pwl)

        self.rounds = rounds

        self.players = self.init_all_players()
        self.alive = list(self.players.keys())

        self.nr_players = len(self.players)

        # self.abundance = self.init_abundance()

    # def init_abundance(self):
    #     tmp = np.ones([self.nr_players, 1]) * (self.population_size / self.nr_players)
    #     return tmp

    # def init_players_randomly(self):
    #     for i in range(self.nr_players):
    #         strategy = np.random.choice([0,1], size=(8,))
    #         decimal = int("".join(map(str, strategy)), 2)
    #         player = Player(strategy, self.rounds)
    #         self.players[decimal] = player
    #     self.alive = list(self.players.keys())


    def init_all_players(self):
        players = {}
        n = 8 # nr of different choises in the game tree
        strategies = [list(i) for i in product([0, 1], repeat=n)] # all binary 9 bit combinations
        initial_abuncance = self.population_size / len(strategies) # initial abundance equally distributed
        for s in strategies:
            player = Player(s, self.rounds)
            player.update_abundance(0, initial_abuncance)
            decimal = int("".join(map(str, s)), 2)
            players[decimal] = player
        return players

    def simulate_game(self, p1, p2, t):
        p1_strategy = p1.get_strategy()
        p2_strategy = p2.get_strategy()

        [p1_utility, p2_utility] = self.game.simulate_game(p1_strategy, p2_strategy)
        p1.update_score(t, p1_utility)
        p2.update_score(t, p2_utility)

    def update_abundance(self, t):
        if(len(self.alive) < 2):
            print('hello')

        sum_points = 0
        for p in self.alive:
            sum_points += self.players[p].utility[t]
        avg_fitness = sum_points / len(self.alive)

        scale_factor = 0
        for p in self.alive:
            last_abundance = self.players[p].abundance[t-1]
            fitness = self.players[p].utility[t]
            alpha = 0.2 # scale factor
            new_abuncance = last_abundance * (1 + alpha * ( fitness - avg_fitness ))
            self.players[p].update_abundance(t, new_abuncance)
            if(new_abuncance < scale_factor):
                scale_factor = new_abuncance
            # sum_abundance += new_abuncance

        sum_abundance = 0
        for p in self.alive:
            updated = self.players[p].abundance[t] + abs(scale_factor)
            self.players[p].update_abundance(t, updated)
            sum_abundance = sum_abundance + updated


        abundance_threshold = 15 #1 / self.population_size
        for p in self.alive:
            normalised_abundance = (self.players[p].abundance[t] / sum_abundance) * self.population_size
            if(normalised_abundance>500):
                print('hello')
            if(normalised_abundance > abundance_threshold):
                self.players[p].update_abundance(t, normalised_abundance)
            else:
                self.players[p].update_abundance(t, 0)
                self.alive.remove(p)

        sum_new_abundance = 0
        for p in self.alive:
            sum_new_abundance = sum_new_abundance + self.players[p].abundance[t]

        for p in self.alive:
            normalised_new_abundance = (self.players[p].abundance[t] / sum_new_abundance) * self.population_size
            if(normalised_new_abundance>500):
                print('hello')
            self.players[p].update_abundance(t, normalised_abundance)


    def simulate_evolution(self):
        for t in range(1, self.rounds):
            for ind, p1 in enumerate(self.alive):
                player_1 = self.players[p1]
                for p2 in self.alive[ind:]:
                    player_2 = self.players[p2]
                    self.simulate_game(player_1, player_2, t)

            self.update_abundance(t)
            print(t, len(self.alive))

            # sum_points = 0
            # for p in self.alive:
            #     sum_player = self.players[p].utility[t]
            #     sum_points += sum_player
            # for p in copy.deepcopy(self.alive):
            #     sum_player = self.players[p].utility[t]
            #     part_player = sum_player/sum_points
            #     if(part_player < 0.002):
            #         self.alive.remove(p)


    def plot_stuff(self):
        plt.title('Two Round Prisoners Evolution')
        ax = plt.subplot(1, 1, 1)
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Utility')
        for key, player in self.players.items():
            # ax.plot(np.linspace(1, len(player.utility[1:]), len(player.utility[1:])), player.utility[1:],
            #         label=str(player.strategy))
            ax.plot(np.linspace(1, len(player.abundance), len(player.abundance)), player.abundance,
                    label=str(player.strategy))
        # handles, labels = ax.get_legend_handles_labels()
        # ax.legend(handles, labels)

        plt.show()
