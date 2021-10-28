birth_year = int(input("What year were you born in?: "))
if birth_year < 1994:
    browser = input("do you remember the GOPHER? ")
    if browser == 'yes' or 'y':
      print("Here's your cane old man.")
    else: print("You're pretty spry for an old guy")
else:
      ipod = input("Did you own an iPod? ")
      if ipod == 'yes' or 'y':
        print("You're pretty cool")
      else:
        print("Better sell that Zune.")
print("Thanks for playing")
