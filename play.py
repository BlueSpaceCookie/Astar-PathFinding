from node import Node
from connection import Connection
from reader import read

import sys

def search(nodes, start, end):
    frontier = []
    history = []
    endNode = nodes[end]

    frontier.append(nodes[start])
    while(frontier):
        node = frontier.pop(0)
        if node.name == endNode.name:
            road = []
            node.getParent(road)
            road.reverse()
            road.append(node.name)
            return road

        children = node.connections
        for child in children:
            
            currentNode = nodes[child.destination]
            currentNode.g = child.distance
            currentNode.h = abs(int(endNode.position[0]) - int(currentNode.position[0]))
            currentNode.f = int(currentNode.g) + int(currentNode.h)

            if(currentNode in history):
                continue

            if(currentNode not in frontier):
                frontier.append(currentNode)
                currentNode.setParent(node)
            elif(currentNode in frontier):
                frontierNode = frontier[frontier.index(currentNode)]
                if(currentNode.g < frontierNode.g):
                    frontier[frontier.index(currentNode)] = currentNode
            
            
        frontier.sort(key=lambda x: x.f)
        history.append(node)
                
if __name__ == "__main__":


    nodes = read()
    x = search(nodes, "Copenhagen", "Genoa")

    print(x)

    
