"""
representation -> Adjacency list: list or dict of length |v|
Adj[u] contains neighbours of u
"""

from collections import defaultdict


# class Vertex:
#     def __init__(self):
#         neighbours = adj[self]

def breadth_first_search(adj : dict ,start : int):
    print("starting search")
    level = {start:0}
    parent = {start: None}
    i = 1
    frontier = [start]
    while frontier:
        next_ = []
        for u in frontier:
            for v in adj[u]: # edges from u to v
                if v not in level:
                    print(v)
                    level[v] = i
                    parent[v] = u
                    next_.append(v)
        frontier = next_
        i=i+1

def main():
    adj = defaultdict({0 : [1,2], 1 : [3,5,7], 2 : [4,1,3], 3 : [1,4,6]})
    start = 0
    breadth_first_search(adj,start)
main()

if '__name__' == '__main__' :
    print("starting")
    main()
    
    
