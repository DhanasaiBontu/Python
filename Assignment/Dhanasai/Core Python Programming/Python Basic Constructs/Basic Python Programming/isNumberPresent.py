
"""python -> Assignments -> Dhanasai Bontu -> Python Basic Constructs (module name) -> 4 folders (for basic questions, data structures, functions,
exception handling) -----> in this way you guys need to create it (refer tejasri's folder in assignment section to get an idea)

upload both pdf and word version for everything you do

for basic questions refer "ML problem" pdf in Assignment section (do any 10) 
for data structures refer "data structures in python-assignment" in assignment section (scenarios questions are there)
for functions refer "functions in python-assignment" in assignment section (scenario based questions)
for exception handling (mentor will upload the questions by night)

submit basic questions and data structures by friday
submit functions and exception handling by monday

in github: push all these folders in git (personal github repo) and make it private (mentor will rreach out to you whenever required)"""


value = int(input("Enter a number to check:"))
data = list(map(int, input("Enter the sample data:").split()))
if value in data:
	print("True")
else:
	print("False")