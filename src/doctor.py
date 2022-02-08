"""
In this class the Doctor person is created.

It is inherited from the Worker person.
"""

from dataclasses import dataclass
from src import worker

@dataclass
class Doctor(worker.Worker):
    __type: str  # Type of work

    @property
    def type(self):  # Getter of __type 
        return self.__type   
    
    @type.setter
    def type(self, setType):  # Setter of __type
        self.__type = setType

    def talk(self):  # Method to print information about the certain person
        print("Hello! I am {} {}. I am a {} that works {} a week and I have a salary of {}.\n".format(self.firstName,self.lastName,
        self.type,self.weeklyHours,self.salary))
