post=input("enter the post:")
if("saad" in post):
    print("this post is talking about saad")
else:
    print("this post is not talking about saad")



#saad is not equal to SAAD or Saad
# in this program i used upper and lower case so thats why when i write Saad or SAAD output will be same 



post=input("enter the post:")
if("saad".upper() in post.upper()):
    print("this post is talking about saad")
else:
    print("this post is not talking about saad")