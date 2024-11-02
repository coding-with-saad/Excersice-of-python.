class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()


# agr hum class method nahi lagye ge to output 45 likhi aye ge kio ke wo latest attribute ha agr hume pehli
#value chahte hain to hume class method chyie ho ga