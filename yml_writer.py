import yaml
import io
from classStructure import player, room
from yml_reader import munchYaml

roomList = munchYaml()

for i in range(0, len(roomList)):
    print(roomList[i])


with io.open('rooms.yml', 'w', encoding='utf8') as outfile:
    for i in range(0, len(roomList)):
        yaml.dump(roomList[i], outfile, sort_keys=False, explicit_start=True, default_flow_style=False, allow_unicode=True)
