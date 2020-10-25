
class Connection:
    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance
    
    def __str__(self):
        return f"Connection: [{self.destination}, {self.distance}]"