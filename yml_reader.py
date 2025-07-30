import yaml
import io
from yaml.loader import SafeLoader
from classStructure import room
roomList = []

def yamlReader():
    # open yaml file for loading
    with open('example.yml', 'r') as f:
        data = list(yaml.load_all(f, Loader=SafeLoader))

    return data

def createRoom(roomId, roomName, description, enemyRoom, exits):
    # from provided yaml data create object room
    roomId = room(roomId, roomName, description)
    roomId.exits = exits
    roomId.enemyRoom = enemyRoom

    # create list of rooms to be called on later
    roomList.append(roomId)

    return roomList

# Print the values as a dictionary
def defineDungeon(data):
    #Loop list of yaml data entries
    for i in range(0,len(data)):

        room = data[i].get('room')
        roomName = data[i].get('roomName')
        description = data[i].get('description')
        enemyRoom = bool(data[i].get('enemyRoom'))
        exits = data[i].get('exits', {})

        #pass each yaml data entry to function
        createRoom(room, roomName, description, enemyRoom, exits)

    return room, roomName, description, enemyRoom, exits

def munchYaml():
    data = yamlReader()
    defineDungeon(data)

    return roomList
