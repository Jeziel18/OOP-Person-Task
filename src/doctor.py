from dataclasses import dataclass
from src import worker

@dataclass
class Doctor(worker.Worker):
    __type: str

    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, setType):
        self.__type = setType

    def talk(self):
        print("Hello! I am {} {}. I am a {} that works {} a week and I have a salary of {}.\n".format(self.firstName,self.lastName,
        self.type,self.weeklyHours,self.salary))
