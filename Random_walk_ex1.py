#%%
#author: Murali
#Random walk model and plotting it on graph

import random

def random_walk(n):

    # n - number of random walks input from user

    x = 0   # starting points
    y = 0
    x_c = [0]
    y_c = [0]

    for i in range(n):
        direction = random.choice(["N","S","E","W"])
        if direction == "N":
            y = y+1
        elif direction == "S":
            y = y-1
        elif direction == "E":
            x = x+1
        else:
            x = x-1
        print("i: ", i, "x: ",x, "y: ",y)
        x_c.append(x)
        y_c.append(y)
    return(x,y,x_c,y_c)

#%% test the output and see final coordinates

x,y,x_c,y_c = random_walk(100)

import matplotlib.pyplot as plt
# print(x,y)
print("max_x: ",max(x_c), "min_x: ",min(x_c))
print("max_y: ",max(y_c), "min_y: ",min(y_c))
plt.plot(x_c, y_c)
plt.show()


#%%
