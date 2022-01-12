from dataclasses import dataclass
from src import worker

@dataclass
class Engineer(worker.Worker):
    type: str
    company: str
    has_master: bool
    has_doctorate: bool

    @property
    def Type(self):
        return self.type

    @Type.setter
    def Type(self, setType):
        self.type = setType

    @property
    def Company(self):
        return self.company

    @Company.setter
    def Company(self, setCompany):
        self.company = setCompany

    def talk(self):
        print("Hello! I am",self.firstName,self.lastName,", I am a",self.Type,"engineer that works",  
        self.weeklyHours,"a week at",self.Company,"and I have a salary of ",self.Salary,".")
        print("I have a master degree:", self.has_master)
        print("I have a doctorate degree:", self.has_doctorate)