# CS-412-Coursework
Coding Assignments from CS 412: Introduction to Data Mining @ UIUC FA'23

Brief Overview:

Homework 3:

This project contains a Python implementation of various machine learning and statistical methods, primarily focusing on classification and cross-validation. Key components of the project include:
1. Naive Bayes Classifier: my_Bayes_candy
   
Functionality: Computes posterior probabilities using the Naive Bayes approach.

Description: This function calculates posterior probabilities by iterating through observed features, adjusting likelihoods based on observed data, and normalizing the results to update prior probabilities iteratively.

3. Data Splitting: get_splits
   
Functionality: Partitions data into k random splits.

Description: This function shuffles a list of item indices and distributes them into k splits. It ensures that each split is approximately equal in size and handles any remaining items by distributing them across the splits.

5. Cross-Validation: my_cross_val
   
Functionality: Performs k-fold cross-validation with various classifiers.

Description: This function evaluates different classifiers by training them on training sets and testing them on test sets derived from cross-validation splits. It calculates and returns the error rates for each classifier, enabling comparison of their performance.

Homework 5:

This code implements a basic version of the PrefixSpan algorithm for mining frequent sequential patterns from data. It includes two primary functions:

1. ord_prefixspan(filename, minsup)
   
Functionality: Extracts frequent sequential patterns from a file of sequences.

Description:
Opens and reads a file where sequences are provided in a specific format.
Extracts sequences using regular expressions, counts the occurrences of each item, and filters items that meet or exceed the minimum support threshold.
For each item that meets the threshold, creates subsets of sequences that follow the item and recursively mines further patterns using the prefix_span_algo function.
Returns a dictionary of frequent sequences and their counts.

3. prefix_span_algo(elem, subset, minsup, freq_sequences)
   
Functionality: Recursively mines frequent sequential patterns by extending prefixes.

Description:
Generates a set of unique items from the current subset of sequences.
For each item, counts its occurrences within the subset. If the count meets or exceeds the minimum support threshold, it extends the current prefix with the item and adds it to the frequent sequences dictionary.
Creates a new subset by removing the current item from the beginning of sequences and recursively applies the function to mine further patterns.
