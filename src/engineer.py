from dataclasses import dataclass
from src import worker

@dataclass
class Engineer(worker.Worker):
    Type: str
    Company: str
    has_master: bool
    has_doctorate: bool

    @property
    def type(self):
        return self.Type

    @type.setter
    def type(self, setType):
        self.Type = setType

    @property
    def company(self):
        return self.Company

    @company.setter
    def company(self, setCompany):
        self.Company = setCompany

    def talk(self):
        print("Hello! I am {} {}, I am a {} engineer that works {} a week at {} and I have a salary of {}.".format(self.firstName,
        self.lastName,self.type,self.weeklyHours,self.company,self.Salary))
        print("I have a master degree: {}".format(self.has_master))
        print("I have a doctorate degree: {}\n".format(self.has_doctorate))