from game import Game
from player import Player

if __name__ == '__main__':
    # """
    # The argument of the 'Player' object is its strategy, according to:
    #
    # 0: always defect
    # 1: always coorporate
    # 2: random
    # 3: tit for tat
    # 4: tit for two tats
    #
    # The values defined below are used to initialise the payoff values throughout the game, where:
    #
    # both_coorporate_utility: equal utility for both players when both corporate
    # WW_winner_utility: utility for winner when both players play war
    # WW_looser_utility: utility for looser when both players play war
    # WP_winner_utility: utility for winner when p1 plays war and p2 plays peace
    # WP_looser_utility: utility for looser when p1 plays war and p2 plays peace
    # PW_winner_utility: utility for winner when p1 plays peace and p2 plays war
    # PW_looser_utility: utility for looser when p1 plays peace and p2 plays war
    #
    #
    # The parameter 'rounds' defines the amount of rounds played in the game.

    # """

    # payoff
    both_coorporate_utility = 2
    WW_winner_utility = 4
    WW_looser_utility = -1
    WP_winner_utility = 2
    WP_looser_utility = -1
    PW_winner_utility = 4
    PW_looser_utility = -2

    rounds = 15000

    game = Game(rounds, both_coorporate_utility, WW_winner_utility, WW_looser_utility, WP_winner_utility,
                WP_looser_utility, PW_winner_utility, PW_looser_utility)

    p1 = Player(3)
    p2 = Player(2)

    game.simulate_2_players(p1, p2)
    game.plot_average_and_accumulated(p1, p2)