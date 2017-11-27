import numpy as np

class Player:

    def __init__(self, strategy=0):
        """

        :param strategy: defines the strategy to be played by the player as
        0: always defect
        1: always coorporate
        2: random
        3: tit for tat
        4: tit for two tats

        default: 0

        """
        start_capital = 100

        self.accumulated_resources = [start_capital]
        self.actions = []
        self.average_utility = []

        self.strategy = strategy

    def alive(self):
        if(self.accumulated_resources > 0):
            return 1
        else:
            return 0


    def get_strategy(self, me, opponent, t):
        if(self.strategy == 0):
            s = self.always_defect(me, opponent, t)
        elif (self.strategy == 1):
            s = self.always_coorporate(me, opponent, t)
        elif (self.strategy == 2):
            s = self.random(me, opponent, t)
        elif (self.strategy == 3):
            s = self.tit_for_tat(me, opponent, t)
        elif (self.strategy == 4):
            s = self.tit_f2_tat(me, opponent, t)
        else:
            s = 0 # default to 0

        self.strategy.append(s)
        return s


    def tit_f2_tat(self, me, opponent, t):
        if (t <= 1):
            return (1)  # cooperate round 0 and 1
        if (opponent[t - 2] == 0 & opponent[t - 1] == 0):
            return (0)  # defect if last two opponent moves were defect
        return (1)  # otherwise cooperate

    def tit_for_tat(self, me, opponent, t):
        if (t == 1):
            return (1)
        return (opponent[t - 1])

    def always_defect(self, me, opponent, t):
        return (0)

    def always_coorporate(self, me, opponent, t):
        return (1)

    def random(self, me, opponent, t):
        return (round(np.random.rand()))