with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("saif" in line):
        print(f"Yes saif is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No saif is not present")