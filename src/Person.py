from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass(init=True)
class Person(ABC):
    first_name: str
    last_name: str
    Age: int
    Gender: str
    Height: str
    Weight: float
    person_counter: int = field(init = False, repr = False, default=0)

    def __post_init__(self):
        Person.person_counter += 1

    @property
    def _fistName(self):
        return self.first_name

    @_fistName.setter
    def _firstName(self, firstName):
        self.first_name = firstName

    @property
    def _lastName(self):
        return self.last_name

    @_lastName.setter
    def _lastName(self, lastName):
        self.last_name = lastName

    @property
    def _age(self):
        return self.Age

    @_age.setter
    def _age(self, setAge):
        self.Age = setAge

    @property
    def _gender(self):
        return self.Gender

    @_gender.setter
    def _gender(self, setGender):
        self.Gender = setGender

    @property
    def _height(self):
        return self.Height

    @_height.setter
    def _height(self, setHeight):
        self.Height = setHeight

    @property
    def _weight(self):
        return self.Weight

    @_weight.setter
    def _weight(self, setWeight):
        self.Weight = setWeight
        
    @abstractmethod
    def talk(self):
        self.talk()







