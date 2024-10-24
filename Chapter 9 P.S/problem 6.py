with open("hub.html","r") as f:
    content=f.read()

if("saif"in content):
    print("saif is present")
else:
    print("saif is not present")