# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import time


both_coorporate_utility = 1
both_defect_utility = 2
looser_utility = -4
winner_utility = 4

a_start_capital = 100
b_start_capital = 100

a_resources = [a_start_capital]
b_resources = [b_start_capital]

a_actions = [1] # to get indexation from 1
b_actions = [1]

a_utility = [a_start_capital]
b_utility = [b_start_capital]

rounds = 500

resolution = 100 # resolution of the map
animate = False # if animate is True, show animations


def init_map():
    im.set_data(np.zeros((resolution, resolution)))

def update_map(i):
    the_map = np.zeros([resolution, resolution])
    a_part = round( resolution * (a_resources[-1] / (a_resources[-1] + b_resources[-1])) )
    the_map[:,:a_part] = 1
    im.set_data(the_map)
    return im



def init_utility_plot():
    ax2.plot(np.linspace(1, len(a_utility), len(a_utility)), a_utility, label='Tit for tat', color='orange')
    ax2.plot(np.linspace(1, len(b_utility), len(b_utility)), b_utility, label='Random', color='blue')

def update_utility_plot(i):
    ax2.plot(np.linspace(1, len(a_utility), len(a_utility)), a_utility, label='Tit for tat', color='orange')
    ax2.plot(np.linspace(1, len(b_utility), len(b_utility)), b_utility, label='Random', color='blue')
    return ax2


if (animate):
    # animation of utility
    fig = plt.figure(1)
    data = np.zeros((resolution, resolution))
    im = plt.imshow(data, vmin=0, vmax=1)



    # animation of utility
    fig2 = plt.figure(2)
    ax2 = fig2.add_subplot(111)

    li_a, = ax2.plot(np.linspace(1, len(a_utility), len(a_utility)), a_utility, label='Tit for tat', color='orange')
    li_b, = ax2.plot(np.linspace(1, len(b_utility), len(b_utility)), b_utility, label='Random', color='blue')
    ax2.set_title('Iteraded prisoners')
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Average Utility')
    handles, labels = ax2.get_legend_handles_labels()
    ax2.legend(handles, labels)
    try:
        anim = animation.FuncAnimation(fig, update_map, init_func=init_map, frames=resolution * resolution,
                                       interval=200)
        anim2 = animation.FuncAnimation(fig2, update_utility_plot, init_func=init_utility_plot,
                                        frames=resolution * resolution,
                                        interval=200)
    except(KeyboardInterrupt):
        pass








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
    if(t == 1):
        return(1)
    return(opponent[t-1])

# play the game the defined amount of rounds
for t in range(1, rounds):
    if(a_resources[-1] <= 0 or b_resources[-1] <= 0):
        # if the resources of any player is less than zero, exit
        break


    a_strategy = 0 # always defect
    b_strategy = round(np.random.rand()) # random strategy
    a_actions.append(a_strategy) # store strategy
    b_actions.append(b_strategy) # store strategy


    if(a_strategy == 0):
        a_tmp = a_resources[-1] - 1 # if action is war, pay war fee
    else:
        a_tmp = a_resources[-1] # otherwise temporarily store the last score
    if(b_strategy == 0):
        b_tmp = b_resources[-1] - 1 # if action is war, pay war fee
    else:
        b_tmp = b_resources[-1] # otherwise temporarily store the last score


    [a_result, b_result] = evaluate_strategy(a_strategy, b_strategy) # evaluate the strategies and get the game result
    a_utility.append((a_tmp + a_result) / t) # store the average result over time
    b_utility.append((b_tmp + b_result) / t)
    
    a_resources.append(a_tmp + a_result) # get the average accumulated resources
    b_resources.append(b_tmp + b_result)

    # if(t%100 == 0):
    #     plt.pause(0.5)



plt.suptitle('Iterated Prisoners')
ax = plt.subplot(1,2,1)
ax.plot(np.linspace(1,len(a_utility), len(a_utility)), a_utility, label='Always Defect')
ax.plot(np.linspace(1,len(b_utility), len(b_utility)), b_utility, label='Random')
ax.set_xlabel('Iterations')
ax.set_ylabel('Average Utility')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# ax = plt.subplot(1,3,2)
# ax.plot(np.linspace(1,len(a_actions), len(a_actions)), a_actions, label='Tit for tat')
# ax.plot(np.linspace(1,len(b_actions), len(b_actions)), b_actions, label='Random')
# ax.set_title('Iteraded prisoners')
# ax.set_xlabel('Iterations')
# ax.set_ylabel('Action')
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, labels)


ax = plt.subplot(1,2,2)
ax.plot(np.linspace(1,len(a_resources), len(a_resources)), a_resources, label='Always Defect')
ax.plot(np.linspace(1,len(b_resources), len(b_resources)), b_resources, label='Random')
ax.set_xlabel('Iterations')
ax.set_ylabel('Accumulated utility')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
plt.show()

