from dataclasses import dataclass
from src import person

@dataclass
class Worker(person.Person):
    __salary: float
    __weekly_hours: float

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, setSalary):
        self.__salary = setSalary

    @property
    def weeklyHours(self):
        return self.__weekly_hours
    
    @weeklyHours.setter
    def weeklyHours(self, setWeeklyHours):
        self.__weekly_hours = setWeeklyHours

    def talk(self):
        print("Hello! I am {} {}, I am a worker that works {} a week and I have a salary of {}.\n".format(self.firstName,
        self.lastName,self.weeklyHours,self.salary))


    
