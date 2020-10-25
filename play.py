from node import Node
from connection import Connection
from reader import read


def zeroHeuristic(currentNode, endNode):
    return 0

def xHeuristic(currentNode, endNode):
    return abs(int(endNode.position[0]) - int(currentNode.position[0]))

def yHeuristic(currentNode, endNode):
    return abs(int(endNode.position[1]) - int(currentNode.position[1]))

def manhattanHeuristic(currentNode, endNode):
    xDistance = abs(int(endNode.position[0]) - int(currentNode.position[0]))
    yDistance = abs(int(endNode.position[1]) - int(currentNode.position[1]))

    return xDistance + yDistance

def asTheCrowFliesHeuristic(currentNode, endNode):
    xDistance = (int(endNode.position[0]) - int(currentNode.position[0]))**2
    yDistance = (int(endNode.position[1]) - int(currentNode.position[1]))**2

    return xDistance + yDistance

def search(nodes, start, end, heuristic = xHeuristic):
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
            currentNode.h = heuristic(currentNode, endNode)
            currentNode.f = int(currentNode.g) + int(currentNode.h)

            if(currentNode in history):
                continue

            if(currentNode not in frontier):
                frontier.append(currentNode)
                currentNode.setParent(node)
            elif(currentNode in frontier):
                frontierNode = frontier[frontier.index(currentNode)]
                if(currentNode.g < frontierNode.g):
                    frontierNode = currentNode
            
            
        frontier.sort(key=lambda x: x.f)
        history.append(node)
                
if __name__ == "__main__":
    nodes = read()
    road = search(nodes, "Copenhagen", "Belgrade", asTheCrowFliesHeuristic)

    print(road)

    
