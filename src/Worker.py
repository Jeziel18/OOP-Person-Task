from dataclasses import dataclass
from src import person

@dataclass
class Worker(person.Person):
    salary: float
    weekly_hours: float

    @property
    def Salary(self):
        return self.salary
    
    @Salary.setter
    def Salary(self, setSalary):
        self.salary = setSalary
