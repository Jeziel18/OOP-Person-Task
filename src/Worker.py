from dataclasses import dataclass
from src import person

@dataclass
class Worker(person.Person):
    Salary: float
    weekly_hours: float

    @property
    def _salary(self):
        return self.Salary
    
    @_salary.setter
    def _salary(self, setSalary):
        self.Salary = setSalary

    @property
    def _weeklyHours(self):
        return self.weekly_hours
    
    @_weeklyHours.setter
    def _weeklyHours(self, setWeeklyHours):
        self.weekly_hours = setWeeklyHours

    def talk(self):
        print("Hello! I am {} {}, I am a worker that works {} a week and I have a salary of {}.\n".format(self._firstName,
        self._lastName,self._weeklyHours,self._salary))


    
