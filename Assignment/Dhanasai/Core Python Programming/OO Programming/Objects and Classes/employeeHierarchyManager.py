class Employee:
    def __init__(self,manager,department):
        self.manager = manager
        self.department = department
    def display(self):
        print(f"Employee: {self.manager} | Department: {self.department}")
class Manager(Employee):
    def __init__(self,manager,department,team_size):
        super().__init__(manager, department)  
        self.team_size = team_size
    def display(self):
        print(f"Manager: {self.manager} | Department: {self.department} | Team Size: {self.team_size}")
m = Manager("Alex", "IT", 10) 
m.display()
    
