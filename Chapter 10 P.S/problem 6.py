# import random.randint
from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    def book(self,fro,to):
        print(f"All train ticket is book for train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on the time 12:00 pm")

    def getfare(self,fro,to):
        print(f"Train ticket fare for train no: {self.trainNo} from {fro} to {to} is {randint(222,1000)}")

t=Train(15)
t.book("Islamabad", "Lahore")
t.getstatus()
t.getfare("Islamabad", "Lahore")