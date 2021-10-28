numberOfFib = int(input("How many Fibonacci numbers do you want to see?: \n"))

n1 = 0
n2 = 1
count = 0

if numberOfFib <=0:
  print("Please enter a positive number")
elif numberOfFib == 1:
  print("This is the first Fibonacci number",numberOfFib,":")
  print(n1)
else:
  print("Finbonacci Sequence: ")
  while count < numberOfFib:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    count = count + 1
