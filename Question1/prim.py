'''
Created on Apr 17, 2014

In this programming problem you'll code up Prim's minimum spanning tree algorithm. Download the text file here. This file describes an undirected graph with integer edge costs. It has the format
[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874. You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

@author: J.Wang
'''
f = open("edges.txt")
line1= f.readline()
from collections import OrderedDict
nodenum, edgenum = [int(x) for x in line1.split()]
#print (nodenum, edgenum) 
edges = {}
for line in f:
    src, tgt, val = [int(y) for y in line.split()]
    if src in edges.keys():
        edges[src].append((tgt, val))
    else:
        edges[src] = [(tgt, val)]
    if tgt in edges.keys():
        edges[tgt].append((src, val))
    else:
        edges[tgt] = [(src, val)]

#print OrderedDict(sorted(edges.items())) 
x = [1]
T = []
while len(x) != nodenum:
    possible = []
    for ele in x:
        #if ele in edges.keys():
        for edge in edges[ele]:
            if edge[0] not in x:
                possible.append(edge)
    sorted_possible = sorted(possible, key = lambda t: t[1])
    v,e = sorted_possible[0]
    x.append(v)
    T.append(e)
    
print sum(T)