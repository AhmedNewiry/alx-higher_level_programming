#!/usr/bin/python3                                                                                           
def best_score(a_dictionary):
    if a_dictionary:
        scores = [value for key, value in a_dictionary.items()]
        scores.sort(reverse=True)
        for key, value in a_dictionary.items():
            if value == scores[0]:
                return key
    return (None)
