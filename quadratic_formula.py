print("ax^2+bx+c=0")
a = float(input("Enter the Leading coefficient: "))
b = float(input("Enter the linear coefficient: "))
c = float(input("Enter the constant: "))
d = b**2-4*a*c
if d>= 0:
  sol1 = (-b-d**.5)/(2*a)
  sol2 = (-b+d**.5)/(2*a)
  print(sol1,sol2)
else:
    print("No Real Solutions")
