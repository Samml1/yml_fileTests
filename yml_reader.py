import yaml
import io

# read yaml file
with open('yml_file.yml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)

print(data_loaded)
