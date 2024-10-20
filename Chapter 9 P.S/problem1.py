f=open("poem.txt")
content=f.read()
if("twinkle" in content):
    print("the word twinkle twinkle little star is in poem")
else:
    print("the word twinkle twinkle little star is not in the poem")
f.close