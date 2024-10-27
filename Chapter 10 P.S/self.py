class Employee: 
    name="saad"                                 # This is a class attribute
    salary=200000
    language="python"
    def getinfo(self):
        print(f"Name is {self.name}, language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning") 
#@staticmethod lagao ya phir self lagao baat aik he ha   
saad=Employee()
saad.greet()                                                     #1 
saad.getinfo()                                                   #2
#these two statements are equal functinality                                   