from src import person
from src import worker
from src import lawyer
from src import doctor
from src import engineer
from src import student

class Main:

   
    person = person.Person("Miguel", "Angel", 25, "Male", "5-10", 135.5, 1)
    worker = worker.Worker("Miguel", "Angel", 25, "Male", "5-10", 135.5, 5000.50, 35.5, 2)
    lawyer = lawyer.Lawyer("Miguel", "Angel", 25, "Male", "5-10", 135.5, 5000.50, 35.5, "Colegio Law Firm", 3)
    doctor = doctor.Doctor("Miguel", "Angel", 25, "Male", "5-10", 135.5, 5000.50, 35.5, "Neurologist", 4)
    engineer = engineer.Engineer("Miguel", "Angel", 25, "Male", "5-10", 135.5, 5000.50, 35.5, "Computer", "UPRM", False, True, 5)
    student = student.Student("Miguel", "Angel", 25, "Male", "5-10", 135.5, "UPRM", "Computer Engineer", 6)

    print(person)
    print(worker)
    print(lawyer)
    print(doctor)
    print(engineer)
    print(student)

    
    
   

    
    

    
    
   