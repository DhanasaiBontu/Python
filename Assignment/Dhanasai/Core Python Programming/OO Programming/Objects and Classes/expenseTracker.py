class ExpenseTracker:
    def __init__(self):
        self.lst = []
    def add_expense(self,amount):
        self.lst.append(amount)
    def total_expense(self):
        return sum(self.lst)
e = ExpenseTracker() 
e.add_expense(200) 
e.add_expense(300) 
print(e.total_expense()) 