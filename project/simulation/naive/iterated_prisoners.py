
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

both_coorporate_utility = 3
both_defect_utility = 1
looser_utility = 0
winner_utility = 3

a_resources = 2
b_resources = 2

a_actions = []
b_actions = []

a_utility = []
b_utility = []

rounds = 20


# Defect: action 0
# Cooperate: action 1

def evaluate_strategy(a, b):
    if(a == 1 and b == 1): # both coorporate
        return(both_coorporate_utility, both_coorporate_utility)
    elif(a == 1 and b == 0): # a coorporate, b defect
        return(looser_utility, winner_utility)
    elif(a == 0 and b == 1): # a defect, be coorporate
        return(winner_utility, looser_utility)
    elif(a == 0 and b == 0): # both defect
        return(both_defect_utility, both_defect_utility)


def tit_for_tat(me, opponent, t):
    if(t == 0):
        return(1)
    return(opponent[t-1])


# play the game the defined amount of rounds
for t in range(rounds):
    a_strategy = tit_for_tat(a_actions, b_actions, t)
    b_strategy = round(np.random.rand()) # random strategy
    a_actions.append(a_strategy)
    b_actions.append(b_strategy)
    [a_result, b_result] = evaluate_strategy(a_strategy, b_strategy)
    a_utility.append(a_result)
    b_utility.append(b_result)

ax = plt.subplot(1,1,1)
ax.plot(np.linspace(1,len(a_utility), len(a_utility)), a_utility, label='Tit for tat')
ax.plot(np.linspace(1,len(b_utility), len(b_utility)), b_utility, label='Random')
ax.set_title('Iteraded prisoners')
ax.set_xlabel('Iterations')
ax.set_ylabel('Utility')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
plt.show()

ax = plt.subplot(1,1,1)
ax.plot(np.linspace(1,len(a_actions), len(a_actions)), a_actions, label='Tit for tat')
ax.plot(np.linspace(1,len(b_actions), len(b_actions)), b_actions, label='Random')
ax.set_title('Iteraded prisoners')
ax.set_xlabel('Iterations')
ax.set_ylabel('Action')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
plt.show()

