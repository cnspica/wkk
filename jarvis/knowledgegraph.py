#coding=utf-8
from entity import Entity
import os, sys, codecs, json, re
from igraph import *

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
    g = Graph()
    g.add_vertices(3)
    # only valid edges can be added
    g.add_edges([(0,1), (1,2), (2,0)])
    g.add_vertices(3)
    g.add_edges([(2,3),(3,4),(4,5),(5,3)])
    print g
    g.get_eid(2,3)
    g.delete_edges(3)
    summary(g)
    g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
    g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
    g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
    g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
    g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]
    print g.degree()
    print g.degree(type='in')
    print 'betweenness: ', g.edge_betweenness()
    print 'pagerank: ', g.pagerank()
    # figure out which connections have the highest betweenness
    ebs = g.edge_betweenness()
    max_eb = max(ebs)
    print [g.es[idx].tuple for idx, eb in enumerate(ebs) if eb == max_eb]
    print g.vs[2].degree()
    print 'select: ',g.vs.select(_degree = g.maxdegree())["name"]
    # find specific node
    claire = g.vs.find(name="Claire")
    print type(claire)
    print claire.index



if __name__ == '__main__':
    testGraph()
