#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    largest = 0
    key_large = ""
    for key, value in a_dictionary.items():
        if value > largest:
            largest = value
            key_large = key
    return (key_large)
