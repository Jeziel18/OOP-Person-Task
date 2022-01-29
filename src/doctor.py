from dataclasses import dataclass
from src import worker

@dataclass
class Doctor(worker.Worker):
    Type: str

    @property
    def _type(self):
        return self.Type
    
    @_type.setter
    def _type(self, setType):
        self.Type = setType

    def talk(self):
        print("Hello! I am {} {}. I am a {} that works {} a week and I have a salary of {}.\n".format(self._firstName,self._lastName,
        self._type,self._weeklyHours,self._salary))
