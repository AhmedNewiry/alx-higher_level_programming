#!/usr/bin/python3
def best_score(a_dictionary):
    scores = sorted([value for key,value in a_dictionary.items()])
    return scores[0]
