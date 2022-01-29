from src import person
from src import worker
from src import lawyer
from src import doctor
from src import engineer
from src import student

class Main:

   
    persona = person.Person("Luisa", "Martinez", 25, "Female", "5-6", 135.5) 
    trabajador = worker.Worker("Miguel", "Sanchez", 41, "Male", "6-0", 167.2, 14484, 35.5)
    abogado = lawyer.Lawyer("Angela", "Rodriguez", 28, "Female", "5-5", 115.8, 50000.50, 40, "Colegio Law Firm")
    doctorxyz = doctor.Doctor("Jose", "Alvarez", 53, "Male", "5-10", 157.6, 110500.30, 40.5, "Neurologist")
    ingeniero = engineer.Engineer("Bienvenido", "Velez", 56, "Male", "5-11", 210.5, 95700.10, 40, "Computer", "UPRM", True, True)
    estudiante = student.Student("Jeziel", "Torres", 22, "Male", "5-10", 151.2, "UPRM", "Computer Engineer")
    
    print("Total people created: {}\n".format(person.Person.person_counter))
    
    persona.talk()
    trabajador.talk()
    abogado.talk()
    doctorxyz.talk()
    ingeniero.talk()
    estudiante.talk()

    grades = [98,52,81,65,77]
    estudiante.calculate(grades)
    
    
    
    

    
    
   

    
    

    
    
   