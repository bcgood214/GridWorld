# Benjamin Good
# 2022-05-07
# Reinforcement learning practice program

# The approach can be described as finding the optimal policy for navigating a grid by approximating the value of each state,
## with the final element being the terminal state.
# An image of the grid this implementation is based on can be found in example 4.1 in the Sutton and Barto text.

import random

rewards = [-1 for i in range(14)]
# Add 0 for the terminal state
rewards.append(0)

# For the value arrays
v = [0 for i in range(15)]
v_next = [0 for i in range(15)]

def take_rand_action(state, ind):
    # 0 = up, 1 = down, 2 = left, 3 = right 
    action = random.randint(0, 3)

    if ind == 14:
        return ind
    elif ind == 0 and action == 2:
        return 14
    elif ind == 3 and action == 0:
        return 14
    elif ind == 10 and action == 1:
        return 14
    elif ind == 13 and action == 3:
        return 14
    elif ind in [3, 7, 11] and action == 2:
        return ind
    elif ind in [2, 6, 10] and action == 3:
        return ind
    elif ind in [11, 12, 13] and action == 1:
        # print("Block down at {}".format(ind))
        return ind
    elif ind in [0, 1, 2] and action == 0:
        return ind
    else:
        if action == 0:
            if ind == 3:
                return 14
            return ind-4
        elif action == 1:
            return ind+4
        elif action == 2:
            # Just in case negative indexing is a no-go
            if ind == 0:
                return 14
            return ind-1
        elif action == 3:
            return ind+1

# 0 = up, 1 = down, 2 = left, 3 = right 
def take_action(action, ind):

    if ind == 14:
        return ind
    elif ind == 0 and action == 2:
        return 14
    elif ind == 3 and action == 0:
        return 14
    elif ind == 10 and action == 1:
        return 14
    elif ind == 13 and action == 3:
        return 14
    elif ind in [3, 7, 11] and action == 2:
        return ind
    elif ind in [2, 6, 10] and action == 3:
        return ind
    elif ind in [11, 12, 13] and action == 1:
        # print("Block down at {}".format(ind))
        return ind
    elif ind in [0, 1, 2] and action == 0:
        return ind
    else:
        if action == 0:
            if ind == 3:
                return 14
            return ind-4
        elif action == 1:
            return ind+4
        elif action == 2:
            # Just in case negative indexing is a no-go
            if ind == 0:
                return 14
            return ind-1
        elif action == 3:
            return ind+1


def episode():
    i = 0
    for state in v_next:
        total = 0
        for j in range(4):
            action = take_action(j, i)
            total += rewards[action] + v_next[action]
        v_next[i] = total/4
        i += 1

def main():
    for i in range(100):
        episode()
    

if __name__ == "__main__":
    main()
    print(v_next)