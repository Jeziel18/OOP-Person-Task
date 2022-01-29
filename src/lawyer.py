from dataclasses import dataclass
from src import worker

@dataclass
class Lawyer(worker.Worker):
    law_firm: str

    @property
    def lawFirm(self):
        return self.law_firm
    
    @lawFirm.setter
    def lawFirm(self, setLawFirm):
        self.law_firm = setLawFirm

    def talk(self):
        print("Hello! I am {} {}, I am a lawyer that works {} a week at {} and I have a salary of {}.\n".format(self.firstName,
        self.lastName,self.weeklyHours,self.lawFirm,self.salary))


