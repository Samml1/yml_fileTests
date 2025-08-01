import yaml
import io
from yml_reader import munchYaml

roomList = munchYaml()

with io.open('rooms.yml', 'w', encoding='utf8') as outfile:
    for i in range(0, len(roomList)):
        yaml.dump(roomList[i], outfile, sort_keys=False, explicit_start=True, default_flow_style=False, allow_unicode=True)
