class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
            print(f"the square of n is {self.n*self.n}")
    def cube(self):
            print(f"the cube of n is {self.n*self.n*self.n}")
    def squareroot(self):
            print(f"the squareroot of n is {self.n**1/2}")
    @staticmethod
    def hello():
          print("Saif hello whats up")

a=calculator(10)
a.hello()
a.square()
a.cube()
a.squareroot()