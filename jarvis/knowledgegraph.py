#coding=utf-8
from entity import Entity
import os, sys, codecs, json, re
import networkx as nx
import matplotlib.pyplot as plt

entityList = [];

def loadEntity(filename):
    entityfile = codecs.open(filename, 'r')
    tmpindex = 1
    namestr = ''
    parentstr = ''
    childstr = ''
    for entityline in entityfile:
        larr = entityline.split('\n',1)
        # print entityline
        if tmpindex == 1:
            namestr = larr[0]
        if tmpindex == 2:
            parentstr = larr[0]
        if tmpindex == 3:
            childstr = larr[0]

        tmpindex = tmpindex + 1

        if entityline[:5] == '#####':
            tmpindex = 1
            entityList.append(createEntity(namestr, parentstr, childstr))




def createEntity(namestr, parentstr, childstr):
    name = namestr.split(' ')
    parent = parentstr.split(' ')
    child = childstr.split(' ')

    entity = Entity(name, parent, child)
    entity.displayEntity()
    return entity


def testLoad():
    tier2filename = 'knowledge/2tier.txt'
    tier3filename = 'knowledge/3tier.txt'
    tier4filename = 'knowledge/4tier.txt'
    tier5filename = 'knowledge/5tier.txt'

    print 'loading tier2 data'
    loadEntity(tier2filename)

    print 'loading tier3 data'
    loadEntity(tier3filename)

    print 'loading tier4 data'
    loadEntity(tier4filename)

    print 'loading tier5 data'
    loadEntity(tier5filename)

def testGraph():
    G = nx.Graph()
    # add one node at a time,
    G.add_node(1)
    # add a list of nodes,
    G.add_nodes_from([2,3])
    # G can also be grown by adding one edge at a time,
    G.add_edge(1,2)
    e=(2,3)
    G.add_edge(*e)
    # adding a list of edges,
    G.add_edges_from([(1,2),(1,3)])
    G.clear()
    # There are no complaints when adding existing nodes or edges. For example, after removing all nodes and edges,
    # we add new nodes/edges and NetworkX quietly ignores any that are already present.
    G.add_edges_from([(1,2),(1,3)])
    G.add_node(1)
    G.add_edge(1,2)
    G.add_node("spam")       # adds node "spam"
    G.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'
    print 'number of nodes: ', G.number_of_nodes()
    print 'number of edges: ', G.number_of_edges()
    print 'Nodes: ', G.nodes()
    print 'Edges: ', G.edges()
    print 'Neighbor 1: ', G.neighbors(1)
    # Removing nodes or edges has similar syntax to adding:
    G.remove_nodes_from("spam")
    print 'Nodes: ', G.nodes()
    G.remove_edge(1,3)
    print 'Edges: ', G.edges()
    #You can safely set the attributes of an edge using subscript notation if the edge already exists
    G.add_edge(1,3)
    G[1][3]['color']='blue'
    # Fast examination of all edges is achieved using adjacency iterators. Note that for undirected graphs this actually looks at each edge twice.
    FG=nx.Graph()
    FG.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
    for n,nbrs in FG.adjacency_iter():
       for nbr,eattr in nbrs.items():
           data=eattr['weight']
           if data<0.5: print('(%d, %d, %.3f)' % (n,nbr,data))

    # Attributes such as weights, labels, colors, or whatever Python object you like, can be attached to graphs, nodes, or edges.
    # Graph attributes
    G = nx.Graph(day="Friday")
    print G.graph
    # you can modify attributes later
    G.graph['day']='Monday'
    print G.graph

    # Node attributes
    # Add node attributes using add_node(), add_nodes_from() or G.node
    G.add_node(1, time='5pm')
    G.add_nodes_from([3], time='2pm')
    print G.node[1]
    G.node[1]['room'] = 714
    print G.nodes(data=True)

    # Edge Attributes
    # Add edge attributes using add_edge(), add_edges_from(), subscript notation, or G.edge.
    G.add_edge(1, 2, weight=4.7 )
    G.add_edges_from([(3,4),(4,5)], color='red')
    G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
    G[1][2]['weight'] = 4.7
    G.edge[1][2]['weight'] = 4
    print G.edges(data=True)

    # Directed graphs
    # The DiGraph class provides additional methods specific to directed edges, e.g. DiGraph.out_edges(), DiGraph.in_degree(), DiGraph.predecessors(), DiGraph.successors() etc.
    DG=nx.DiGraph()
    DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])
    print DG.out_degree(1,weight='weight')
    print DG.degree(1,weight='weight')
    print DG.successors(1)
    print DG.neighbors(1)

    # Drawing graphs
    # nx.draw(G)
    # nx.draw_random(G)
    # nx.draw_circular(G)
    # nx.draw_spectral(G)
    # nx.draw_networkx_labels(G, (1, 2, 3, 4, 5))
    # plt.show()
    # plt.savefig("path.png")




if __name__ == '__main__':
    testGraph()
