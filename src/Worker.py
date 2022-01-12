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

    @property
    def weeklyHours(self):
        return self.weekly_hours
    
    @weeklyHours.setter
    def weeklyHours(self, setWeeklyHours):
        self.weekly_hours = setWeeklyHours

    def talk(self):
        print("Hello! I am",self.firstName,self.lastName,", I am a worker that works",  
        self.weeklyHours,"a week and I have a salary of ",self.Salary,".")


    
