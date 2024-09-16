import random
import numpy as np
from xgboost import XGBClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def get_splits(n, k, seed):
    splits = None # given
    # Implement your code to construct the splits here
    random.seed(seed) # set to random value
    splits = [] # changed
    listIndices = list(range(n)) # builds a list of given item indices
    random.shuffle(listIndices) # shuffles indices using random function
    size = n // k # size of each split is items / number of splits
    for i in range(k): # loop through number of splits
        start_val = i * size # set start size
        end_val = (i + 1) * size # set end_val size
        temp_split = listIndices[start_val:end_val] # distribute items
        splits.append(temp_split) # append to splits
    for j in range(n % k): # remaining items
        splits[j].append(listIndices[k * size + j]) # append to splits
    return splits # return

def my_cross_val(method, X, y, splits):
    errors = [] # given
    # Implement your code to calculate the errors here
    state_const = 412 # stored var b/c every random_state = 412
    for fold in splits: # loop through each fold in our cross-validation
        flag_arr = np.setdiff1d(np.arange(X.shape[0]), fold) # bool arr, shows indices in curr fold
        X_training_set, X_testing_set = X[flag_arr], X[fold] # training and testing set for X
        y_training_set, y_testing_set = y[flag_arr], y[fold] # training and testing set for y
        # these conditionals select appropriate method and use params specified by hw doc
        if method == 'XGBClassifier': 
            classifier_val = XGBClassifier(max_depth = 5, random_state = state_const)
        if method == 'SVC':
                classifier_val = SVC(gamma = 'scale', C = 10, random_state = state_const)
        if method == 'LinearSVC':
                classifier_val = LinearSVC(max_iter = 2000, random_state = state_const)
        if method == 'LogisticRegression':
                classifier_val = LogisticRegression(penalty = 'l2', solver = 'lbfgs', random_state = state_const, multi_class = 'multinomial')
        if method == 'RandomForestClassifier':
                classifier_val = RandomForestClassifier(max_depth = 20, n_estimators = 500, random_state = state_const)
        classifier_val.fit(X_training_set, y_training_set) # train using training data
        y_prediction = classifier_val.predict(X_testing_set) # predict labels using testing data
        error_rate = np.mean(y_prediction != y_testing_set) # error rate using labels vs actual labels
        errors.append(error_rate) # each calculated error rate is appended into array
    return np.array(errors) # given, ret list of error rates