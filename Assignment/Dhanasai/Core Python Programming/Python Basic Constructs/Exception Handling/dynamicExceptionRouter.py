def handle_value_error(value):
	return f"Handled by ValueError Function: {value}"
def handle_type_error(value):
	return f"Handled by TypeError function: {value}"
def handle_error(error_type, value):
	handlers = {
		"ValueError":handle_value_error,
		"TypeError" :handle_type_error
	}
	try:
		handler = handlers[error_type]
		return handler(value)
	except KeyError:
		return "Unknown"
	finally:
		print("Error Handled")
handle_error("ValueError","bad")