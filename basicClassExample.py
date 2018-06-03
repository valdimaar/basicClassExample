class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = first
        self.email = first + "." + last + "@example.com"
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
emp_1 = Employee("John", "Smith", 50000)
emp_2 = Employee("Matthew", "Parks", 100000)

print(emp_2.fullname())
