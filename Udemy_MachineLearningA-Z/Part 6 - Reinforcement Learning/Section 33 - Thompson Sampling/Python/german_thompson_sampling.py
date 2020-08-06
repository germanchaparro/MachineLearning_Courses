# Thompson Sampling

#%% Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#%% Implementing Thompson Sampling
import random
N = 500                                # 478 is the minimum value I found in which the algortihm chooses Ad 4
d = 10
ads_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
total_reward = 0

for n in range(0, N):
    selected_ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            selected_ad = i
            max_random = random_beta
    ads_selected.append(selected_ad)
    
    reward = dataset.values[n, selected_ad]
    if reward == 1:
        numbers_of_rewards_1[selected_ad] += 1
    else:
        numbers_of_rewards_0[selected_ad] += 1
        
    total_reward += reward

#%% Visualising the results - Histogram
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()