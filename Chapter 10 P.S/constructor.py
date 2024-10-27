class Employee: 
    name="Saad"                                 # This is a class attribute
    salary=200000
    language="python"
    def __init__(self,name,salary,language):    # dunder method which is automatically called ya haar bari chle ga
        self.name=name
        self.language=language
        self.salary=salary    
        print("saif is op")
                                 
saad=Employee("saad",13000,"java script")
print(saad.name,saad.language,saad.salary)
# print(f"Name is {saad.name}, language is {saad.language} and salary is {saad.salary}")
# saif=Employee()
# print(saif.name)