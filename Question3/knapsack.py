'''
Created on Apr 21, 2014

In this programming problem and the next you'll code up the knapsack algorithm from lecture. Let's start with a warm-up. Download the text file here. This file describes a knapsack instance, and it has the following format:
[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]
...
For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.
You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

@author: J.Wang
'''
import sys
sys.setrecursionlimit(10000) 
f = open("knapsack1.txt")
line1 = f.readline()
size, num = [int(x) for x in line1.split()]
#print size, num
items = []
for line in f:
    v, w  = line.split()
    v,w = int(v), int(w)
    items.append((v,w))

def knapsack(W, items):
    # bottom-up solution
    N = len(items)
    A = [[0 for _ in xrange(W)] for _ in xrange(N)]
    for i in xrange(N):
        v, w = items[i]
        for j in xrange(W):
            if j-w < 0: A[i][j] = A[i-1][j]
            else: A[i][j] = max(A[i-1][j], A[i-1][j-w] + v)
    return A[N-1][W-1]

def knapsack_optimized(W, items):   
    # top-down solution with memoization via hashtable;
    # applicable for large problem instances
    N = len(items)
    A = {}
    def A_(i, j):
        if (str(i)+','+str(j)) in A: return A[str(i)+','+str(j)] # memoization
        if i == 0: return 0
        v, w = items[i]
        if j-w < 0: 
            result = A_(i-1, j)
            A[str(i)+','+str(j)] = result # memoization
            return result
        else:
            result = max(A_(i-1, j), A_(i-1, j-w) + v)
            A[str(i)+','+str(j)] = result # memoization
            return result
    return A_(N-1, W-1)

result = knapsack_optimized(size, items)
print result