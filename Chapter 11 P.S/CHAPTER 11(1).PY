class employee:                                          #Base class
    name="jjj"
    company="saif"
    def show(self):
        print(f"name is{self.name} and company is {self.salary} ")


# class programer:
#     company="op"
#     def show(self):
#         print(f"the boy is good{self.name} and this bad{self.salary}")


#     def nice(self):
#         print(f"the boy is fasj{self.name} and this fE{self.salary}")
class programmer(employee):                                             #inhertance class
    company="op"
    def show(self):
        print(f"the boy is good{self.name} and this bad{self.salary}")



a=employee()
b=programmer()
print(a.company,b.company)

      