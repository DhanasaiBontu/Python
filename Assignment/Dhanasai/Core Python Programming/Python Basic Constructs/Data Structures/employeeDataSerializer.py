employee_data = [("Alex", "IT"), ("Riya", "HR")]
serialized_data = [{'name':name, 'department':dept} for name, dept in employee_data]
print(serialized_data)