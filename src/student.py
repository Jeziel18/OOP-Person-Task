from dataclasses import dataclass
from src import person

@dataclass
class Student(person.Person):
    Institution: str
    Major: str

    @property
    def institution(self):
        return self.Institution

    @institution.setter
    def institution(self, setIntitution):
        self.Institution = setIntitution

    @property
    def major(self):
        return self.Major

    @major.setter
    def major(self, setMajor):
        self.Major = setMajor    

    def calculate(self, kwargs):
        result = sum(kwargs) / len(kwargs)
        print("Grades Average: {}\n".format(result))

    def talk(self):
        print("Hello! I am {} {}. I am a student at {}, studying {}.".format(self.firstName,self.lastName,
        self.institution,self.major))
