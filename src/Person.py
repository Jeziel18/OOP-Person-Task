"""
In this class the Person is created. This is the base model
for the other persons to be created.

It used abtrasct classes for the method talk().
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass(init=True)
class Person(ABC):
    __first_name: str  #  first name
    __last_name: str  # last name
    __age: int  # age of the person
    __gender: str  # gender of the person
    __height: str  # height of the person
    __weight: float  # weight of the person
    person_counter: int = field(init = False, repr = False, default=0)  # Method to count persons created

    def __post_init__(self):  # initialization of the person_counter
        Person.person_counter += 1

    # All the Getter and Setters for each atribute of the person

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
    def talk(self):  # Abstract method to print information about certain person
        pass







