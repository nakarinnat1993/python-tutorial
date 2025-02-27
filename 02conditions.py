score = 55
name = "John"

if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50 and name == "Jo":
    print(name+": D")
else:
    print(name+": F")