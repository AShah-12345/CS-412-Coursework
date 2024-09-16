# CS-412-Coursework
Coding Assignments from CS 412: Introduction to Data Mining @ UIUC FA'23

Brief Overview:

Homework 3:

This project contains a Python implementation of various machine learning and statistical methods, primarily focusing on classification and cross-validation. Key components of the project include:
1. Naive Bayes Classifier: my_Bayes_candy
Functionality: Computes posterior probabilities using the Naive Bayes approach.
Parameters:
pi_list: Prior probabilities for each class.
p_list: Likelihood of observed features for each class.
c_list: Observed features or draws.
Description: This function calculates posterior probabilities by iterating through observed features, adjusting likelihoods based on observed data, and normalizing the results to update prior probabilities iteratively.
2. Data Splitting: get_splits
Functionality: Partitions data into k random splits.
Parameters:
n: Total number of items.
k: Number of desired splits.
seed: Random seed for reproducibility.
Description: This function shuffles a list of item indices and distributes them into k splits. It ensures that each split is approximately equal in size and handles any remaining items by distributing them across the splits.
3. Cross-Validation: my_cross_val
Functionality: Performs k-fold cross-validation with various classifiers.
Parameters:
method: Classifier method to use (e.g., XGBClassifier, SVC, LogisticRegression, etc.).
X: Feature matrix.
y: Labels.
splits: Indices for training and testing splits.
Description: This function evaluates different classifiers by training them on training sets and testing them on test sets derived from cross-validation splits. It calculates and returns the error rates for each classifier, enabling comparison of their performance.
