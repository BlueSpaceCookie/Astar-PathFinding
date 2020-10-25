from node import Node
from connection import Connection
from graphviz import Digraph

def read():
    nodes = {}
    positionsFile = open("positions.txt", "r")
    connectionsFile = open("connections.txt", "r")

    cities = positionsFile.read().split("\n")
    connections = connectionsFile.read().split("\n")

    for city in cities:
        data = city.split(" ")
        node = Node(data[0], [data[1], data[2]])
        for connection in connections:
            cityConnection = connection.split(" ")
            if(node.name == cityConnection[0]):
                link = Connection(cityConnection[1], cityConnection[2])
                node.addConnection(link)
            elif(node.name == cityConnection[1]):
                link = Connection(cityConnection[0], cityConnection[2])
                node.addConnection(link)
        nodes[node.name] = node
    return nodes

def makeGraph(nodes):
    graph = Digraph()
    for node in nodes.values():
        graph.node(node.name, node.name)
        for connection in node.connections:
            graph.edge(node.name, connection.destination, connection.distance)
    
    graph.render("test.gv", view = True)


if __name__ == "__main__":
    nodes = read()


    

    

    
    
    


