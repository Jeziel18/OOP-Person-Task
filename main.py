from src import person
from src import worker
class Main:

   
    person = person.Person("Miguel", "Angel", 25, "Male", "5-10", 135.5)
    worker = worker.Worker("Miguel", "Angel", 25, "Male", "5-10", 135.5, 5000.50, 35.5)

    print(person)
    print(worker)
    
   