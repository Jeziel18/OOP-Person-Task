from dataclasses import dataclass
from src import worker

@dataclass
class Engineer(worker.Worker):
    Type: str
    Company: str
    has_master: bool
    has_doctorate: bool

    @property
    def _type(self):
        return self.Type

    @_type.setter
    def _type(self, setType):
        self.Type = setType

    @property
    def _company(self):
        return self.Company

    @_company.setter
    def _company(self, setCompany):
        self.Company = setCompany

    def talk(self):
        print("Hello! I am {} {}, I am a {} engineer that works {} a week at {} and I have a salary of {}.".format(self._firstName,
        self._lastName,self._type,self._weeklyHours,self._company,self._salary))
        print("I have a master degree: {}".format(self.has_master))
        print("I have a doctorate degree: {}\n".format(self.has_doctorate))