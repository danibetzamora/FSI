# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

pa = search.GPSProblem('P', 'A'
                       , search.romania)

us = search.GPSProblem('U', 'S'
                       , search.romania)

tp = search.GPSProblem('T', 'P'
                       , search.romania)

hs = search.GPSProblem('H', 'S'
                       , search.romania)

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())
print("Problema A - B")
print("------------------------------------------------------------------------")
print(search.branch_and_bound_graph_search(ab).path())
print("\n")
print(search.branch_and_bound_understimation_graph_search(ab).path())
print("------------------------------------------------------------------------\n\n")

print("Problema P - A")
print("------------------------------------------------------------------------")
print(search.branch_and_bound_graph_search(pa).path())
print("\n")
print(search.branch_and_bound_understimation_graph_search(pa).path())
print("------------------------------------------------------------------------\n\n")

print("Problema T - P")
print("------------------------------------------------------------------------")
print(search.branch_and_bound_graph_search(tp).path())
print("\n")
print(search.branch_and_bound_understimation_graph_search(tp).path())
print("------------------------------------------------------------------------\n\n")

print("Problema H - S")
print("------------------------------------------------------------------------")
print(search.branch_and_bound_graph_search(hs).path())
print("\n")
print(search.branch_and_bound_understimation_graph_search(hs).path())
print("------------------------------------------------------------------------\n\n")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
