import yaml
import io
from classStructure import player, room
from yml_reader import munchYaml

roomList = munchYaml()

print(roomList)

'''# Write YAML file
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
'''
