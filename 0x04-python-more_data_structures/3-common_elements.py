#!/usr/bin/python3
def common_elements(set_1, set_2):
    return {i for i, j in zip(set_1, set_2) if i == j}
