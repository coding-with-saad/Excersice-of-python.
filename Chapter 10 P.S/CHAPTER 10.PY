class Employee: 
    name="saad"         # This is a class attribute
    clas=2
    language="python"

saad=Employee()
saad.name="op"        # This is a instance attribute
print(saad.name,saad.language,saad.clas)

saif=Employee()
saif.name="saif op bolte hain"
saif.language="java script"
print(saif.language,saif.name,saif.clas)
# Here name is instance attribute and salary and language are class attributes as they directly belong to the class
#first we will set the class attribute if the instance attribute is set in the program than the class attribute will not work