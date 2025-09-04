# text manipulation programme 
# yaml to json 
import yaml
import json

osList = {}

with open("./operating-systems.yml", 'r') as infile, open("python_operating-systems.json", 'w') as outfile:
  yaml_object = yaml.safe_load(infile)
  json.dump(infile, outfile)

