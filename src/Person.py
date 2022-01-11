from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    gender: str
    height: str
    weight: float
    #check the person_count attribute
    #Class attribute that will count each person that is created. Increment in constructor.

    @property
    def fistName(self):
        return self.first_name

    @fistName.setter
    def firstName(self, firstName):
        self.first_name = firstName

    @property
    def lastName(self):
        return self.last_name

    @lastName.setter
    def lastName(self, lastName):
        self.last_name = lastName

    @property
    def Age(self):
        return self.age

    @Age.setter
    def Age(self, setAge):
        self.age = setAge

    @property
    def Gender(self):
        return self.gender

    @Gender.setter
    def Gender(self, setGender):
        self.gender = setGender

    @property
    def Height(self):
        return self.height

    @Height.setter
    def Height(self, setHeight):
        self.height = setHeight

    @property
    def Weight(self):
        return self.weight

    @Weight.setter
    def Weight(self, setWeight):
        self.weight = setWeight







