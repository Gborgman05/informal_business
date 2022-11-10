#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    store = {}
    for edge in edges:
        if edge[0] in store:
            store[edge[0]] = store[edge[0]] + [edge[0]]
        else:
            store[edge[0]] = [edge[1]]
    fringe = [s]
    distances = [-1 for node in range(n)]
    count = 1
    while fringe:
        cur = fringe.pop(0)
        neighbors = store[cur]
        for neighbor in neighbors:
            if not neighbor:
                distances[neighbor]= count
                for n in store[neighbor]:
                    if not distances[neighbor]:
                        fringe.append(neighbor)
            
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
