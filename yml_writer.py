import yaml
import io
from classStructure import player, room

user1 = player("TestName", "entrance")

# Create the dungeon rooms
entrance = room('entrance','Dungeon Entrance', 'The Entrance to the dungeon')
hallway = room('hallway','Dungeon hallway', 'A dark wet hallway that smells of mildew')
treasureRoom = room('treasureRoom','Treasure Room', 'A room full of a horde of treasure')

# Create exits
entrance.exits["north"] = hallway
hallway.exits["south"] = entrance
hallway.exits["east"] = treasureRoom
treasureRoom.exits["west"] = hallway

# Create enemy rooms
entrance.enemyRoom = False
hallway.enemyRoom = False
treasureRoom.enemyRoom = True

roomList = [entrance, hallway, treasureRoom]

# strip class data to present for yaml file
def tokeniseClass(objectList):
    for i in range(len(objectList)):
        print(roomList[i].id)
        print(roomList[i].roomName)
        print(roomList[i].description)
        exitid=str(roomList[i].exits.values()).lstrip("dict_values([").rstrip("])")
        print(exitid)
        print(str(roomList[i].enemyRoom) + "\n")


tokeniseClass(roomList)


with io.open('rooms.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(roomList[0], outfile, explicit_start=True, default_flow_style=False, allow_unicode=True)
