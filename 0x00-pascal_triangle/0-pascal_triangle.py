#!/usr/bin/python3
'''
Module to generate Pascal's Triangle
'''


def pascal_triangle(n):
    '''
    Returns a list of lists representing Pascal's Triangle
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
