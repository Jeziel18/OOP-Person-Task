"""
This project consists of making an OOP program in python.

The task of the project was to create a collection of people.
People have different ages, works, salaries and names.

The main task is to created and object of a person dynamically for later use to
created different people with different attributes. 

The Dataclasses were used to simplify the use of code. The different person
inherit from the base person to minimize the use of repetition code.

Every person needs to be created, have information about them and use the method talk().
In the talk() method every person is going to print information about them. 
"""

from src import doctor
from src import engineer
from src import lawyer
from src import person
from src import student
from src import worker

class Main:
    """
    This class is used to test the code

    Each person is created and given atributes. Then the method talk() is called.
    With this each person prints information about them.

    The person_counter prints the amount of persons created.

    the calculate() prints the average of a number.
    """
    trabajador = worker.Worker("Miguel", "Sanchez", 41, "Male", "6-0", 167.2, 14484, 35.5)
    abogado = lawyer.Lawyer("Angela", "Rodriguez", 28, "Female", "5-5", 115.8, 50000.50, 40, "Colegio Law Firm")
    doctorxyz = doctor.Doctor("Jose", "Alvarez", 53, "Male", "5-10", 157.6, 110500.30, 40.5, "Neurologist")
    ingeniero = engineer.Engineer("Bienvenido", "Velez", 56, "Male", "5-11", 210.5, 95700.10, 40, "Computer", "UPRM", True, True)
    estudiante = student.Student("Jeziel", "Torres", 22, "Male", "5-10", 151.2, "UPRM", "Computer Engineer")
    
    print("Total people created: {}\n".format(person.Person.person_counter))
    
    trabajador.talk()
    abogado.talk()
    doctorxyz.talk()
    ingeniero.talk()
    estudiante.talk()

    estudiante.calculate(98,52,81,65,77)



    
    
    
    
    

    
    
   

    
    

    
    
   