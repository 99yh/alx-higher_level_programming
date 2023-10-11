#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is not dict:
        return None

    best = None
    best_score = 0
    for student, score in a_dictionary.items():
        if score > best_score:
            best = student
            best_score = score
    return best
