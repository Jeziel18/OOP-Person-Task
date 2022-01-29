from dataclasses import dataclass
from src import worker

@dataclass
class Lawyer(worker.Worker):
    law_firm: str

    @property
    def _lawFirm(self):
        return self.law_firm
    
    @_lawFirm.setter
    def _lawFirm(self, setLawFirm):
        self.law_firm = setLawFirm

    def talk(self):
        print("Hello! I am {} {}, I am a lawyer that works {} a week at {} and I have a salary of {}.\n".format(self._firstName,
        self._lastName,self._weeklyHours,self._lawFirm,self._salary))


