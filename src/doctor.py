from dataclasses import dataclass
from src import worker

@dataclass
class Doctor(worker.Worker):
    type: str

    @property
    def Type(self):
        return self.type
    
    @Type.setter
    def Type(self, setType):
        self.type = setType

    def talk(self):
        print("Hello! I am",self.firstName,self.lastName,", I am a",self.Type,"that works",  
        self.weeklyHours,"a week and I have a salary of",self.Salary,".")
