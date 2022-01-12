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
        print("Hello! I am",self.firstName,self.lastName,", I am a lawyer that works",
        self.weeklyHours,"a week at",self.lawFirm,"and I have a salary of",self.Salary,".")


