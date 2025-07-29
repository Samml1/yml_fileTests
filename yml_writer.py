import yaml
import io
from classStructure import player

user1 = player("TestName", "entrance")

# Write YAML file
with io.open('data.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(user1, outfile, default_flow_style=False, allow_unicode=True)
