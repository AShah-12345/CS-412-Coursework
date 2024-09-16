import math 
import numpy as np 
def my_Bayes_candy(pi_list, p_list, c_list):
    # posterior_probabilities = [[0] * 5 for _ in range(10)] # Default initialization with 0s
    # Implement your code to calculate the posterior probabilities here
    posterior_probabilities = np.zeros((len(c_list), len(pi_list))) # removed default case
    # replaced with 2D array initialization of zeros of size bags from pi_list and draws from c_list
    for i in range(len(c_list)): # loop thru number of draws
        if c_list[i] == 0: # if draw is 0, likelihood is a success
            likelihood = p_list # if success, p_list probability is likelihood
        else: # else,
            if c_list[i] != 0: # if draw is not 0, not a success
                likelihood = 1 - p_list # likelihood is 1 - p_list
        normalization = np.sum(pi_list * likelihood) # add all values of pi_list * likelihood as normalization value
        posterior_probabilities[i] = (pi_list * likelihood) / normalization # calculate using posterior prob equation
        pi_list = posterior_probabilities[i] # update pi_list with posterior prob
    return posterior_probabilities # return posterior prob