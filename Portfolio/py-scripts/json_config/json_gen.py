import json

with open("test_envirnment.json", 'r') as file:
    j_data = json.load(file)

with open("test_envirnment.json", 'w') as file:
    json.dump(j_data, file, indent=4)
