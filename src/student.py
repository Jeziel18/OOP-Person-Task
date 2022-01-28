from dataclasses import dataclass
from src import person

@dataclass
class Student(person.Person):
    institution: str
    major: str

    @property
    def Institution(self):
        return self.institution

    @Institution.setter
    def Institution(self, setIntitution):
        self.institution = setIntitution

    @property
    def Major(self):
        return self.major

    @Major.setter
    def Major(self, setMajor):
        self.major = setMajor    

    def calculate(self, kwargs):
        print(kwargs)

    def talk(self):
        print("Hello! I am",self.firstName,self.lastName,". I am a student at",self.Institution,
        ", studying",self.Major,".")
