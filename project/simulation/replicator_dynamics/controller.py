from replicator_dynamics import ReplicatorDynamics

if __name__ == '__main__':
    # """
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
    # both_coorporate_utility = 2
    # WW_winner_utility = 9
    # WW_looser_utility = -3
    # WP_winner_utility = 15
    # WP_looser_utility = -2
    # PW_winner_utility = 2
    # PW_looser_utility = -5

    both_coorporate_utility = 2
    WW_winner_utility = 8
    WW_looser_utility = -6
    WP_winner_utility = 12
    WP_looser_utility = -5
    PW_winner_utility = 0
    PW_looser_utility = 0

    rounds = 20000

    replicator_dynamics = ReplicatorDynamics(rounds, both_coorporate_utility, WW_winner_utility, WW_looser_utility, WP_winner_utility,
                WP_looser_utility, PW_winner_utility, PW_looser_utility)

    replicator_dynamics.init_game_matrix()
    replicator_dynamics.simulate_dynamics()
