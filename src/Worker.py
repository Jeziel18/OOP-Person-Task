from dataclasses import dataclass
from src import person

@dataclass
class Worker(person.Person):
    Salary: float
    weekly_hours: float

    @property
    def salary(self):
        return self.Salary
    
    @salary.setter
    def salary(self, setSalary):
        self.Salary = setSalary

    @property
    def weeklyHours(self):
        return self.weekly_hours
    
    @weeklyHours.setter
    def weeklyHours(self, setWeeklyHours):
        self.weekly_hours = setWeeklyHours

    def talk(self):
        print("Hello! I am {} {}, I am a worker that works {} a week and I have a salary of {}.\n".format(self.firstName,
        self.lastName,self.weeklyHours,self.salary))


    
