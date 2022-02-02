from dataclasses import dataclass
from src import person

@dataclass
class Student(person.Person):
    __institution: str
    __major: str

    @property
    def institution(self):
        return self.__institution

    @institution.setter
    def institution(self, setIntitution):
        self.__institution = setIntitution

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, setMajor):
        self.__major = setMajor    

    def calculate(self, *args):
        result = sum(args) / len(args)
        print("Grades Average: {}\n".format(result))

    def talk(self):
        print("Hello! I am {} {}. I am a student at {}, studying {}.".format(self.firstName,self.lastName,
        self.institution,self.major))
