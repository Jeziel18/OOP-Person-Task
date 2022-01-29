from dataclasses import dataclass
from src import person

@dataclass
class Student(person.Person):
    Institution: str
    Major: str

    @property
    def _institution(self):
        return self.Institution

    @_institution.setter
    def _institution(self, setIntitution):
        self.Institution = setIntitution

    @property
    def _major(self):
        return self.Major

    @_major.setter
    def _major(self, setMajor):
        self.Major = setMajor    

    def calculate(self, *args):
        result = sum(args) / len(args)
        print("Grades Average: {}\n".format(result))

    def talk(self):
        print("Hello! I am {} {}. I am a student at {}, studying {}.".format(self._firstName,self._lastName,
        self._institution,self._major))
