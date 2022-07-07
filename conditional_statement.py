'''
age = int(input("please provide me your age"))
if age>18:
    pass      #if pass kei audaina output ma 
    #print(f"as your age is {age} and you can watch thor")
else:
    print(f"as your age is {age} and you cannot watch thor")


import random
winning_number = random.randint(0,100)
guessed_number = int(input("enter a number between 1 to 100"))
if guessed_number == winning_number:
    print ("you win the game as number matched")
else:
    if guessed_number>winning_number:
        print ("your guess is high")
    else:
        print ("your guess is less")
print ("the real number by computer is",winning_number)


# and // or 

name, age = input("enter user name and age using comma").split(",")
namee = name.lower()
if namee[0]=="a" and int(age)>18:
    print("you can watch thor")
else:
    print("you cannot watch thor")



age ==> 0-5 ===> free
age ===> 5-60 ==> 200
age ====> 60+ .===>100



age = int(input("enter your age"))
if 0<age<5:
    print("you do not need to pay, it is free")
elif 5<age<60:
    print("you need to pay 200rupees")
elif age>60:
    print("you need to pay 100rupees")
else:
    print ("please enter valid age")



# in and check for empty string

fname = "thor"
sname = ""

if "h" in fname:
    print(f"'h' is present in your name")
else:
    print("iu3wg")



fname = input("please enter your first")

if fname:
    if "a" in fname:
        print ("a is present in your name")
    else:
        print ("not present")
else:
    print ("please enter your name")

'''






