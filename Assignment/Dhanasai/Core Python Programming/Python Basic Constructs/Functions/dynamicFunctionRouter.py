def invoke(command_name, commands_dict):
	if command_name in commands_dict:
		return commands_dict[command_name]()
	else:
		return "Command not found"
print(invoke("start",{"start":lambda:"System started"}))