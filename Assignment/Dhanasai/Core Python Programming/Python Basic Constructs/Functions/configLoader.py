def load_config(config, key, default_value=None):
	return config.get(key, default_value)
print(load_config({"timeout":10},"timeout"))