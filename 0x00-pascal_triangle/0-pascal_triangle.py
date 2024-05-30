#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    pascal triangle of n:
    we assume n will be always an integer
    """
    pascal = []

    if n <= 0:
        return []

    for i in range(n):
        if (i == 0):
            pascal.append([1])
        else:
            cur_row = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    cur_row.append(1)
                else:
                    cur_row.append(pascal[i - 1][j - 1] +
                                   pascal[i - 1][j])

            pascal.append(cur_row)

    return (pascal)
