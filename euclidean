#coding competition in-clas practice

def areCoprime(num1, num2):
  minuend = max(num1, num2)
  subtrahend = min(num1, num2)
  difference = minuend - subtrahend
  print(str(minuend)+" - "+str(subtrahend)+" = "+str(difference))
  if difference == 0:
    return minuend == 1 and subtrahend ==1
  else:
    return True and areCoprime(subtrahend, difference)

if areCoprime(10, 17):
  print("COPRIME")
else:
  print("NOT COPRIME")


if areCoprime(56, 26):
  print("COPRIME")
else:
  print("NOT COPRIME")
