class Employee: 
    name="saad"         # This is a class attribute
    clas=2
    language="py"

saad=Employee
print(saad.name,saad.language,saad.clas)

saif=Employee()
print(saif.language,saif.name,saif.clas)
# Here name is instance attribute and salary and language are class attributes as they directly belong to the class
