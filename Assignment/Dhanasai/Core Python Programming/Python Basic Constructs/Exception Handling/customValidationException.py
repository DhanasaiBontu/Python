class InvalidAgeError(Exception):
	pass

def validate_age(age):
	if age<18 or age>100:
		raise InvalidAgeError("Age must be between 18 and 100")
	return "Valid"
validate_age(15)
