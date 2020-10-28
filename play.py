from node import Node
from connection import Connection
from reader import read
from math import sqrt


def zeroHeuristic(currentNode, endNode):
    return 0

def xHeuristic(currentNode, endNode):
    return abs(int(currentNode.position[0]) - int(endNode.position[0]))

def yHeuristic(currentNode, endNode):
    return abs(int(currentNode.position[1]) - int(endNode.position[1]))

def manhattanHeuristic(currentNode, endNode):
    return xHeuristic(currentNode, endNode) + yHeuristic(currentNode, endNode)

def asTheCrowFliesHeuristic(currentNode, endNode):
    xDistance = (int(endNode.position[0]) - int(currentNode.position[0]))**2
    yDistance = (int(endNode.position[1]) - int(currentNode.position[1]))**2

    return sqrt(xDistance + yDistance)


def search(nodes, start, end, heuristic = xHeuristic):

    frontier = []
    history = []
    startNode = nodes[start]
    endNode = nodes[end]
    counter = 0

    """Contiendra les distances total entre le depart et chaque noeud parcouru"""
    G = {startNode.name : 0}

    """Noeud de depart dans frontier"""
    frontier.append(startNode)
    while(frontier):
        counter = counter + 1

        node = frontier.pop(0)

        """Si le nom du noeud est le meme que celui du noeud de destination le chemin est return"""
        if node.name == endNode.name:
            road = []
            node.getParent(road)
            road.reverse()
            road.append(node.name)
            print(f"Nombre de ville visitée: {counter}")
            return road
        
        """Recuperation des enfants du noeud"""
        children = node.connections
           
        for child in children:
            currentNode = nodes[child.destination]

            """Calcul de g, h et f"""
            currentNode.g = G[node.name] + int(child.distance)
            currentNode.h = heuristic(currentNode, endNode)
            currentNode.f = int(currentNode.g) + int(currentNode.h)
            
            """Si le noeud courant est dans l'historique on continue"""
            if(currentNode in history):
                continue
            
            """Si le noeud courant n'est pas dans frontier on l'ajoute"""
            if(currentNode not in frontier):
                currentNode.setParent(node)
                frontier.append(currentNode)
                G[currentNode.name] = currentNode.g

            """Si le noeud courant est dans frontier on test si le g actuel est meilleur que celui present dans le dictionnaire"""
            if(currentNode in frontier):
                if(currentNode.g < G[currentNode.name]):
                    currentNode.setParent(node)
                    frontier.append(currentNode)
                    G[currentNode.name] = currentNode.g

        """Le noeud est mis dans historique et le tableau frontier est trie selon les valeurs de f"""
        history.append(node)
        frontier.sort(key=lambda x: x.f)
    
    return "Error: pas de chemin trouvé"

                
if __name__ == "__main__":
    """Creation du graph"""
    nodes = read()

    """Recherche du chemin optimal"""
    road = search(nodes, "Paris", "Prague", asTheCrowFliesHeuristic)

    print(road)


