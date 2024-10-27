class programmer:
    company="microsoft"
    def __init__(self,name,salary,language,company,crew):
        self.name=name
        self.salary=salary
        self.language=language
        self.company=company
        self.crew=crew
        # print("This is a manager SAAD  I")
p=programmer("SAAD",1500,"Python","Microsoft",1)
print(p.name,p.company,p.language,p.crew,p.salary)
s=programmer("Saif",500,"java script","meta",2)
print(s.name,s.company,s.language,s.crew,s.salary)