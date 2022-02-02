from dataclasses import dataclass
from src import worker

@dataclass
class Engineer(worker.Worker):
    __type: str
    __company: str
    __has_master: bool
    __has_doctorate: bool

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, setType):
        self.__type = setType

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, setCompany):
        self.__company = setCompany

    def talk(self):
        print("Hello! I am {} {}, I am a {} engineer that works {} a week at {} and I have a salary of {}.".format(self.firstName,
        self.lastName,self.type,self.weeklyHours,self.company,self.salary))
        print("I have a master degree: {}".format(self.__has_master))
        print("I have a doctorate degree: {}\n".format(self.__has_doctorate))