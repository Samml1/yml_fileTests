import yaml
import io
from classStructure import player, room

user1 = player("TestName", "entrance")

# Create the dungeon rooms
entrance = room('Dungeon Entrance', 'The Entrance to the dungeon')
hallway = room('Dungeon hallway', 'A dark wet hallway that smells of mildew')
treasureRoom = room('Treasure Room', 'A room full of a horde of treasure')

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

# Write YAML file
with io.open('player.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(user1, outfile, default_flow_style=False, allow_unicode=True)

with io.open('rooms.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(roomList[0], outfile, explicit_start=True, default_flow_style=False, allow_unicode=True)
