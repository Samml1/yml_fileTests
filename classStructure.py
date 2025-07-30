class player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location

class room(object):
    def __init__(self, name, roomName, description):
        self.name = name
        self.roomName = roomName
        self.description = description
        self.enemyRoom = False
        self.exits = {}
