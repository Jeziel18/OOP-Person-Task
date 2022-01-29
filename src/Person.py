from dataclasses import dataclass, field

@dataclass(init=True)
class Person:
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
    def age(self):
        return self.Age

    @age.setter
    def age(self, setAge):
        self.age = setAge

    @property
    def gender(self):
        return self.Gender

    @gender.setter
    def gender(self, setGender):
        self.gender = setGender

    @property
    def height(self):
        return self.Height

    @height.setter
    def height(self, setHeight):
        self.height = setHeight

    @property
    def weight(self):
        return self.Weight

    @weight.setter
    def weight(self, setWeight):
        self.weight = setWeight

    def talk(self):
        print("Hello! I am {} {}, I have {} and I am a {}. My heigth is {} and my weight is {}.\n".format(self.firstName,
        self.lastName,self.age,self.gender,self.height,self.weight))







