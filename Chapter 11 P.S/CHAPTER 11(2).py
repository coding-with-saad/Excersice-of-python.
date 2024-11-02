class employee:                                          #Base class
    name="jjj"
    company="saif"
    def show(self):
        print(f"name is{self.name} and company")

class coder:
    language="python"
    def printlanguages(self):
        print(f"here is language{self.language}")


class programmer(employee,coder):                                             #inhertance class
    company="op"
    def showlanguage(self):
        print(f"the boy is good{self.name} and this bad")



a=employee()
b=programmer()
# print(a.company,b.company)
b.show()
b.printlanguages()
b.showlanguage()



      