def normalize_names(name_list):
	normalized=[]
	for name in name_list:
		normalized.append(name.strip().lower())
	return normalized
print(normalize_names(["John","MARY","ALex"]))