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
        self.utility = []

        self.strategy = strategy
        self.strategy_name = ""
        self.set_strategy_name()

    def alive(self):
        if(self.accumulated_resources[-1]> 0):
            return 1
        else:
            return 0

    def update_history(self, u, s, t):
        self.actions.append(s)
        self.utility.append(u)
        avg = sum(self.utility) / t
        self.average_utility.append(avg)
        resource = self.accumulated_resources[-1] + u
        self.accumulated_resources.append(resource)


    def get_strategy(self, me, opponent, t):
        if(self.strategy == 0):
            return self.always_defect(me, opponent, t)
        elif (self.strategy == 1):
            return self.always_coorporate(me, opponent, t)
        elif (self.strategy == 2):
            return self.random(me, opponent, t)
        elif (self.strategy == 3):
            return self.tit_for_tat(me, opponent, t)
        elif (self.strategy == 4):
            return self.tit_f2_tat(me, opponent, t)
        else:
            return 0 # default to 0


    def set_strategy_name(self):
        if(self.strategy == 0):
            self.strategy_name = 'Always defect'
        elif (self.strategy == 1):
            self.strategy_name = 'Always cooporate'
        elif (self.strategy == 2):
            self.strategy_name = 'Random'
        elif (self.strategy == 3):
            self.strategy_name = 'Tit for tat'
        elif (self.strategy == 4):
            self.strategy_name = 'Tit for two tats'


    def tit_f2_tat(self, me, opponent, t):
        if (t <= 2):
            return (1)  # cooperate round 0 and 1
        if (opponent[-2] == 0 and opponent[-1] == 0):
            return (0)  # defect if last two opponent moves were defect
        return (1)  # otherwise cooperate

    def tit_for_tat(self, me, opponent, t):
        if (t <= 1):
            return (1)
        return (opponent[-1])

    def always_defect(self, me, opponent, t):
        return (0)

    def always_coorporate(self, me, opponent, t):
        return (1)

    def random(self, me, opponent, t):
        return (round(np.random.rand()))