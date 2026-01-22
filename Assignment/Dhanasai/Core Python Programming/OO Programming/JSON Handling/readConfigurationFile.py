import json
with open("readConfigurationFile.json", "r") as file:
    config_data = json.load(file)
print(config_data["app_name"])