import re # import reg expression python module
from collections import Counter # import counter class from collections module
def ord_prefixspan(filename, minsup): 
    freq_sequences = {} # default initialization
    # complete your code

    with open(filename, 'r') as file: # open file as read only
        scan = [re.search(', <(.*)>', line).group(1) for line in file]
        # scan sequences uses re, omitting '<' and '>', separating by commas
    all_elems = [elem for sequence in scan for elem in sequence]
    # converting extracted sequences into a list
    occurrences = Counter(all_elems)
    # counting occurences of each elem in the list
    maxsup = set() # init empty set to store minsup elems
    for elem, counter in occurrences.items(): # loop through elem and counter in occurrences
        if counter >= minsup: # check if count >= minsup
            maxsup.add(elem) # add satisfied items to maxsup set

    for elem in maxsup: # loop thru elements in maxsup
        subset = [sequence[sequence.index(elem) + 1:] for sequence in scan if elem in sequence]
        # create a subset based on maxsup elements
        freq_sequences[elem] = len(subset)
        # count occurrences of subset and store it in final return freq_sequences
        prefix_span_algo(elem, subset, minsup, freq_sequences)
        # recusrive call prefix_span_algo to mine patterns

    return freq_sequences # return freq_sequences dict


def prefix_span_algo(elem, subset, minsup, freq_sequences): # recursive function for pattern mining
    unique_items = {val for sequence in subset for val in sequence} # set of unique items
    for item in unique_items: # iterate through items in unique_items
        item_count = sum(1 for seq in subset if item in seq) # count occurrences of each item in subset
        if item_count >= minsup: # check if items >= minsup
            prefix_appended = elem + item # if so, append item to prefix
            freq_sequences[prefix_appended] = item_count # store count in freq_sequences dict
            new_subset = [seq[seq.index(item) + 1:] for seq in subset if item in seq] 
            # create new subset with appended prefix
            prefix_span_algo(prefix_appended, new_subset, minsup, freq_sequences)
            # recursively call function again as long as conditions satisfied


    