from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass(init=True)
class Person(ABC):
    __first_name: str
    __last_name: str
    __age: int
    __gender: str
    __height: str
    __weight: float
    person_counter: int = field(init = False, repr = False, default=0)

    def __post_init__(self):
        Person.person_counter += 1

    @property
    def firstName(self):
        return self.__first_name

    @firstName.setter
    def firstName(self, firstName):
        self.__first_name = firstName

    @property
    def lastName(self):
        return self.__last_name

    @lastName.setter
    def lastName(self, lastName):
        self.__last_name = lastName

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, setAge):
        self.__age = setAge

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, setGender):
        self.__gender = setGender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, setHeight):
        self.__height = setHeight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, setWeight):
        self.__weight = setWeight
        
    @abstractmethod
    def talk(self):
        pass







