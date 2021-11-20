#!/usr/bin/env python3

import numpy as np
from numpy.core.fromnumeric import sort
from functools import cmp_to_key
import random


global new_compares
global old_compares
new_compares = 0
old_compares = 0

def sort_fun(index_1, index_2):
    global matrix_compare
    global string_list
    global new_compares
    global old_compares

    if matrix_compare[index_1][index_2] == 0:
        r = (string_list[index_1] > string_list[index_2]) * 2 - 1  # todo, get info from user
        print("new  compare ", string_list[index_1], " > ", string_list[index_2], " ", r)
        new_compares += 1
        matrix_compare[index_1][index_2] = r
        matrix_compare[index_2][index_1] = -r

        matrix_compare = find_transitive_pairs(matrix_compare)
    else:
        r = matrix_compare[index_1][index_2]
        print(" old compare ", string_list[index_1], " > ", string_list[index_2], " ", r)
        old_compares += 1

    return r


def find_transitive_pairs(matrix_compare):
    length = len(matrix_compare)
    for i0 in range(0, length):
        for i1 in range(0, length):
            for i2 in range(0, length):
                if i0 == i1 or i1 == i2 or i0 == i2:
                    continue
                if matrix_compare[i0][i1] != 0 and matrix_compare[i1][i2] != 0:
                    # print("(", i0, i1, " ", f'{matrix_compare[i0][i1]:+0.0f}',"), (", i1, i2, " ",f'{matrix_compare[i1][i2]:+0.0f}', ")")
                    if matrix_compare[i0][i1] == matrix_compare[i1][i2] != 0:

                        # set transitive
                        matrix_compare[i0][i2] = matrix_compare[i0][i1]
                        matrix_compare[i2][i0] = matrix_compare[i0][i1]

    return matrix_compare


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
        "A", "B", "C", "D", "E",  "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    ]

    list_indices = [i for i, _ in enumerate(string_list)]

    [string_list, string_list] = shuffle_both(string_list, string_list)
    # string_list = ["B", "D", "C", "E", "A"]  # use same shuffle
    print(string_list)

    matrix_compare = np.zeros((len(string_list), len(string_list)))

    list_indices.sort(key=cmp_to_key(sort_fun))

    for i in list_indices:
        print(string_list[i], end=", ")
    print()

    # print(matrix_compare)

    # for r, _ in enumerate(string_list):
    #     for c, _ in enumerate(string_list):
    #         if r == c:
    #             continue
    #         sort_fun(r, c)

    # print(matrix_compare)

    print("new_compares", new_compares)
    print("old_compares", old_compares)


if __name__ == "__main__":
    main()
