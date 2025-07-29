class room(object):
    def __init__(self, roomName, description):
        self.roomName = roomName
        self. description = description
        self.exits = {}
        self.enemies = {}
        self.enemyRoom = False
