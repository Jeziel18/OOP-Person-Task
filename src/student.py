"""
In this class the Student person is created.

It is inherited from the Person class.
"""

from dataclasses import dataclass
from src import person

@dataclass
class Student(person.Person):
    __institution: str  # institution the students goes to
    __major: str  # the major od study of the student

    # Getters and Setters for the Student atributes

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

    def calculate(self, *args):  # Method to calculate the averge of given ints
        result = sum(args) / len(args)
        print("Grades Average: {}\n".format(result))

    def talk(self):  # Method to print information about the certain person
        print("Hello! I am {} {}. I am a student at {}, studying {}.".format(self.firstName,self.lastName,
        self.institution,self.major))
