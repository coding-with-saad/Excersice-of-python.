# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l

# l=["saif","saad","sabi","an"]
# print(rem(l,"sabi"))







def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n   

        

l=["saif","saad","sabi","an"]
print(rem(l,"sabi"))