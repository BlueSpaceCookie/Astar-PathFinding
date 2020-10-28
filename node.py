
class Node:
    def __init__(self, name = None, position = None):
        self.name = name
        self.position = position
        self.connections = []
        self.parent = None

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        if(self.name != other.name):
            return False
        if(self.position != other.position):
            return False
        if(self.connection != other.connections):
            return False
        if(self.g != other.g):
            return False
        if(self.h != other.h):
            return False
        if(self.f != other.f):
            return False
        return True

    def __str__(self):
        output =  f"Node: [Name = {self.name}, Distance = {self.name}, Position = {self.position}, Connection = ["
        for x in self.connections:
            output += x.__str__()
        output += f"], Parent = {self.parent}, g = {self.g}, h = {self.h}, f = {self.f}]"
        return output

    def setParent(self, parent):
        self.parent = parent

    def getParent(self, road):
        if self.parent is not None:
            road.append(self.parent.name)
            self.parent.getParent(road)

    def addConnection(self, connection):
        self.connections.append(connection)
    