def DivByFive():
    a = [361,   636,    277, 	129, 	434, 	577, 	796, 	596, 	727, 	566, 
    156, 	109, 	714, 	716, 	546, 	979, 	366, 	766, 	137, 	243, 
    331, 	999, 	922, 	304, 	657, 	314, 	634, 	303, 	677, 	597, 
    363, 	174, 	431, 	193, 	361, 	677, 	403, 	926, 	279, 	692, 
    749, 	401, 	346, 	202, 	763, 	314, 	333, 	244, 	796, 	697, 
    674, 	651, 	517, 	349, 	337, 	667, 	617, 	464, 	379, 	793, 
    542, 	464, 	962, 	146, 	946, 	199, 	302, 	699, 	606, 	126, 
    519, 	203, 	137, 	517, 	146, 	724, 	696, 	699, 	747, 	663, 
    126, 	247, 	469, 	953, 	396, 	502, 	562, 	647, 	364, 	214, 
    346, 	646, 	331, 	426, 	763, 	291, 	557, 	764, 	939, 	656, 
    753, 	561, 	797, 	224, 	537, 	361, 	263, 	493, 	196, 	162, 
    362, 	102, 	629, 	936, 	663, 	279, 	966, 	241, 	907, 	677, 
    945, 	416, 	122, 	563, 	667, 	394, 	654, 	592, 	977, 	177, 
    666, 	199, 	463, 	561, 	954, 	924, 	991, 	363, 	754, 	754, 
    199, 	451, 	796, 	566, 	629, 	651, 	517, 	167, 	704, 	749, 
    622, 	299, 	466, 	559, 	973, 	243, 	639, 	276, 	603, 	753, 
    ]
    b = 1
    print("Array Loaded.  Testing...")
    for x in a:
        b = x*b
    if str(b).endswith("5"):
        print("True")
    elif str(b).endswith("0"):
        print("True")
    else :
        print("False")


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def analyze_ring_graph(numberOfNodes):
    #Make an empty graph
    a_ring = {}
    n=numberOfNodes

    #Add in the edges
    for i in range(n):
        make_link(a_ring, i, (i+1)%n)

    #How many nodes?
    print(len(a_ring))

    #How many edges?
    print(sum([len(a_ring[node]) for node in a_ring.keys()])/2)
    print(a_ring)


def analyze_square_grid_graph(numberOfNodes):
    #Make an empty graph
    a_grid = {}
    n=numberOfNodes

    #Add in the edges
    for i in range(n):
        make_link(a_grid, i, (i+1)%n)

    #How many nodes?
    print("Total Nodes: ", len(a_grid))
    print("Total Nodes on each side: ", n/4)
    print("Total Nodes * 2: ", n*2)
    print("Total Nodes * 2 minus 2 * edge nodes, +1: ", (n*2) - (2*(n/4)) + 1)
    
    #How many edges?  Each will have 2 connections, except the right hand
    # and the bottom edges.  They will each have 1, and the final node will have 0
    edgeNodes = n/4
    print(sum([len(a_grid[node]) for node in a_grid.keys()])-(2*edgeNodes)-2)
    print(a_grid)


import math
def square_graph_solution(numberOfNodes):
    #Make an empty graph
    G = {}
    n = numberOfNodes
    side = int(math.sqrt(n))

    #Add in the edges
    for i in range(side):
        for j in range(side):
            if i < side-1: make_link(G, (i,j), (i+1,j))
            if j < side-1: make_link(G, (i,j), (i,j+1))

    #How many nodes?
    print(len(G))

    #How many edges?
    print(sum([len(G[node]) for node in G.keys()])/2)
