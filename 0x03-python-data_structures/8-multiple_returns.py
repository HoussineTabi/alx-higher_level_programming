#!/usr/bin/python3
def multiple_returns(sentence):
    """this function returns informations about a sentence"""
    len_sentence = len(sentence)
    first_char = None
    if len_sentence != 0:
        first_char = sentence[0]
    return (len_sentence, first_char)
