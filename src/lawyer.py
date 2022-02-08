"""
In this class the Lawyer person is created.

It is inherited from the Worker person.
"""

from dataclasses import dataclass
from src import worker

@dataclass
class Lawyer(worker.Worker):
    __law_firm: str  # Law firm where he works.

    @property
    def lawFirm(self):  # Getter of __law_firm
        return self.__law_firm
    
    @lawFirm.setter
    def lawFirm(self, setLawFirm):  # Setter of __law_firm
        self.__law_firm = setLawFirm

    def talk(self):  # Method to print information about the certain person
        print("Hello! I am {} {}, I am a lawyer that works {} a week at {} and I have a salary of {}.\n".format(self.firstName,
        self.lastName,self.weeklyHours,self.lawFirm,self.salary))


