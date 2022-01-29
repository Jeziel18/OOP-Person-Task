from dataclasses import dataclass
from src import worker

@dataclass
class Doctor(worker.Worker):
    Type: str

    @property
    def type(self):
        return self.Type
    
    @type.setter
    def type(self, setType):
        self.Type = setType

    def talk(self):
        print("Hello! I am {} {}. I am a {} that works {} a week and I have a salary of {}.\n".format(self.firstName,self.lastName,
        self.type,self.weeklyHours,self.salary))
