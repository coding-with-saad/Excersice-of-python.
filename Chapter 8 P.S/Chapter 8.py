# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# Function Definition
# def avg():
#     a = int(input("Enter your number: "))
#     b = int(input("Enter your number: "))
#     c = int(input("Enter your number: "))
    
#     average = (a + b + c)/3
#     print(average)
# avg()     # Function call





# #   Quick quiz
# def goodday():    # def/len/print is a built in function and good day() is user defined function
#     print("good day")

# goodday()




# def goodday(NAME):
#     print("good day, ".upper()+ NAME)

# goodday("SAIF")



# def goodday(NAME,ENDING):
#     print("good day, ".upper()+ NAME)
#     print(ENDING)
#     return "done"

# a=goodday("SAIF","op in the chat")
# print(a)
# goodday("SAAD","op")
# print(a)
# goodday("SABI","op chat")
# print(a)





# def goodday(NAME,ENDING ="THANK YOU"):
#     print("good day, ".upper()+ NAME)
#     print(ENDING)
# goodday("SAIF")






#           RECURSION
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n=int(input("enter a number:"))
print(f"The factorial of this number is: {factorial(n)}")
    



