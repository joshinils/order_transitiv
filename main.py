#!/usr/bin/env python3

import numpy as np
from numpy.core.fromnumeric import sort
from functools import cmp_to_key
import random

def sort_fun(index_1, index_2):
    global matrix_compare
    global string_list

    if matrix_compare[index_1][index_2] == 0:
        r = (string_list[index_1] > string_list[index_2]) * 2 -1 # todo, get info from user
        print("new  compare ", string_list[index_1], " > ", string_list[index_2], "  ", index_1, " > ", index_2, " ", r)
        matrix_compare[index_1][index_2] =  r
        matrix_compare[index_2][index_1] = -r
    else:
        r = matrix_compare[index_1][index_2]
        print(" old compare ", string_list[index_1], string_list[index_2], r)
    return r

def shuffle_both(a, b):
    z = [i for i in zip(a, b)]
    random.shuffle(z)

    [a, b] = zip(*z)
    a = list(a)
    b = list(b)

    return a, b

def main():
    global string_list
    global matrix_compare

    string_list = [
        "A",
        "B",
        "C",
        "D",
    ]
    list_indices = [i for i, _ in enumerate(string_list)]

    [string_list, list_indices] = shuffle_both(string_list, list_indices)
    print(string_list)

    matrix_compare = np.zeros((len(string_list), len(string_list)))

    list_indices.sort(key=cmp_to_key(sort_fun))
    
    for i in list_indices:
        print(string_list[i], end = ", ")
    print()

    print(matrix_compare)


if __name__ == "__main__":
    main()
