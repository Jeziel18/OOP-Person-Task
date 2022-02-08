"""
In this class the Engineer person is created.

It is inherited from the Worker person.
"""

from dataclasses import dataclass
from src import worker

@dataclass
class Engineer(worker.Worker):
    __type: str  # type of work
    __company: str  # company where the person works.
    __has_master: bool  # checks if it has a master degree.
    __has_doctorate: bool  # checks if it has a doctorated degree. 

    @property
    def type(self):  # Getter of __type
        return self.__type  

    @type.setter  # Setter of __type
    def type(self, setType):
        self.__type = setType

    @property
    def company(self):  # Getter of __company
        return self.__company

    @company.setter  # # Setter of __company
    def company(self, setCompany):
        self.__company = setCompany

    def talk(self):  # Method to print information about the certain person
        print("Hello! I am {} {}, I am a {} engineer that works {} a week at {} and I have a salary of {}.".format(self.firstName,
        self.lastName,self.type,self.weeklyHours,self.company,self.salary))
        print("I have a master degree: {}".format(self.__has_master))
        print("I have a doctorate degree: {}\n".format(self.__has_doctorate))