#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    if len_sentence == 0:
        first_char = None
    else:
        first_char = sentence[0]
    my_tuple = (len_sentence, first_char)
    return my_tuple
