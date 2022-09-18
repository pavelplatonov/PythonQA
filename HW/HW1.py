vote = input("Write your geometry (Cube, Trio, Circle):")
line = "*" * 9
stena = "*" + " " * 7 + "*"
cube = line + "\n" + stena + "\n" + stena + "\n" + line
error = "This is not Cube, Trio or Circle"

if vote == "Cube":
    print(cube)
elif vote == "Trio":  # треугольник не доделан и брошен на произвол
    print(line)
elif vote == "Circle":  # круг не доделан и брошен на произвол
    print(stena)
else:
    print(error)
