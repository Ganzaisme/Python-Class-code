word = input("Enter a word: ")
frequency = {}
  
for i in word:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
  
print ("the frequency of each letter of your word is:\n "  +  str(frequency))
