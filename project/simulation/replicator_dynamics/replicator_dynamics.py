from itertools import product

import numpy as np
import matplotlib.pyplot as plt

from game import Game

class ReplicatorDynamics:
    def __init__(self, rounds, bc, www, wwl, wpw, wpl, pww, pwl):

        self.game = Game(bc, www, wwl, wpw, wpl, pww, pwl)
        self.rounds = rounds

        n = 8  # nr of different choises in the game tree
        self.strategies = [list(i) for i in product([0, 1], repeat=n)]  # all binary 8 bit combinations
        self.nr_strategies = len(self.strategies)

        self.game_matrix = np.zeros([self.nr_strategies, self.nr_strategies])

        self.population_size = 1000
        self.abundance = np.asmatrix(np.zeros([self.nr_strategies, self.rounds]))

    def create_game_matrix(self):
        for ind1, p1_strategy in enumerate(self.strategies):
            for ind2, p2_strategy in enumerate(self.strategies):
                score_p1 = []
                score_p2 = []
                for i in range(500): # average score over 500 played games
                    [p1_utility, p2_utility] = self.game.simulate_game(p1_strategy, p2_strategy)
                    score_p1.append(p1_utility)
                    score_p2.append(p2_utility)
                self.game_matrix[ind1][ind2] = np.mean(score_p1)
                self.game_matrix[ind2][ind1] = np.mean(score_p2)
            print(ind1)
        self.abundance = np.asmatrix(self.abundance)
        np.save('game_matrix', self.game_matrix)

    def init_game_matrix(self):
        try:
            gmtx = np.load('game_matrix.npy')
            self.game_matrix = gmtx
        except:
            self.create_game_matrix()

    def init_abundance(self):
        initial_abundance = self.population_size / self.nr_strategies
        self.abundance[:,0] = initial_abundance

    def simulate_dynamics(self):
        self.init_abundance()

        for t in range(1, self.rounds):
            expected_payoff = self.game_matrix * self.abundance[:,t-1]
            mean_fitness = np.mean(self.game_matrix * self.abundance[:,t-1])
            alpha = 0.2
            next_abundance = np.multiply(self.abundance[:,t-1], alpha * (expected_payoff - mean_fitness))
            self.abundance[:,t] = self.abundance[:,t-1] + next_abundance

            # remove individuals lower than threshold
            for ind, a in enumerate(self.abundance[:,t]):
                threshold = 1 #/ self.population_size
                if(a < threshold):
                    self.abundance[ind, t] = 0

            # normalise to original population size
            sum_abundance = np.sum(self.abundance[:, t])
            for ind, a in enumerate(self.abundance[:,t]):
                self.abundance[ind, t] = (a / sum_abundance) * self.population_size

            if(t%1000 == 0):
                print(t)

        self.plot_stuff()

    def plot_stuff(self):


        plt.title('Two Round Prisoners Evolution')
        ax = plt.subplot(1, 1, 1)
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Abundance')
        for ind, a in enumerate(self.abundance):
            ax.plot(np.linspace(1, len(np.asarray(a)[0]), len(np.asarray(a)[0])), np.asarray(a)[0], label="{0:b}".format(ind))
            if(np.asarray(a)[0][-1] > 0):
                print('Strategy: %s - abundance: %i' % ("{0:b}".format(ind), np.asarray(a)[0][-1]))
        # handles, labels = ax.get_legend_handles_labels()
        # ax.legend(handles, labels)

        plt.show()


