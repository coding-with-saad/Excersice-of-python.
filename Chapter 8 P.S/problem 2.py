# f=int(input("enter a number :"))
# c=5*(f-32)/9
# print(c)





#  2nd method
def f_to_c(f):
    return 5*(f-32)/9
f=int(input("enter temperature in f :"))
print(f"{f_to_c(f)} °C")