import yaml
import io
from yaml.loader import SafeLoader
from classStructure import room
from functools import reduce
roomList = []

def yamlReader(fileName):
    # open yaml file for loading
    with open(fileName + '.yml', 'r') as f:
        data = list(yaml.load_all(f, Loader=SafeLoader))

    return data

def createExits(roomlist):
    for i in range(0, len(roomList)):
        print(roomList[i].name)
        for j in range(0,len(roomList)):
            if roomList[j].name in roomList[i].exits.values():
                for x in roomList[i].exits:
                    if roomList[i].exits[x] == roomList[j].name:
                        roomList[i].exits[x] = roomList[j]

    for y in range(0, len(roomList)):
        print(roomList[y].name, roomList[y].exits)



def createRoom(roomId, roomName, description, enemyRoom, exits):
    # from provided yaml data create object room
    roomId = room(roomId, roomName, description)
    roomId.enemyRoom = enemyRoom
    roomId.exits = exits

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
        exits = reduce(lambda union, next_dict: union.update(next_dict) or union, exits, {})

        #pass each yaml data entry to function
        createRoom(room, roomName, description, enemyRoom, exits)

    return room, roomName, description, enemyRoom, exits

def munchYaml():
    fileName=input("Which file to read?\n")
    data = yamlReader(fileName)
    defineDungeon(data)
    createExits(data)

    print(roomList)
    return roomList
