from src import person
from src import worker
from src import lawyer
from src import doctor
from src import engineer
from src import student

class Main:

   
    persona = person.Person("Miguel", "Angel", 25, "Male", "5-10", 135.5) 
    trabajador = worker.Worker("Miguel", "Angel", 25, "Male", "5-10", 135.5, 5000.50, 35.5)
    abogado = lawyer.Lawyer("Miguel", "Angel", 25, "Male", "5-10", 135.5, 5000.50, 35.5, "Colegio Law Firm")
    doctorxyz = doctor.Doctor("Miguel", "Angel", 25, "Male", "5-10", 135.5, 5000.50, 35.5, "Neurologist")
    ingeniero = engineer.Engineer("Miguel", "Angel", 25, "Male", "5-10", 135.5, 5000.50, 35.5, "Computer", "UPRM", False, True)
    estudiante = student.Student("Miguel", "Angel", 25, "Male", "5-10", 135.5, "UPRM", "Computer Engineer")
    
    grades = [98,52,81,65,77]
    estudiante.calculate(grades)
    

    
    persona.talk()
    trabajador.talk()
    abogado.talk()
    doctorxyz.talk()
    ingeniero.talk()
    estudiante.talk()
    print(person.Person.person_counter)
    
    

    
    
   

    
    

    
    
   