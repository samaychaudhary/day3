'''i = 0
while i<10:
    print(f"hello world {i}")
    i += 1     #i=i+1


#for i in range(10):     #10 means only till 9

#for i in range(0,10):      #0 to 9

for i  in range(0,10,2):         #this 0 to 9 with step2
    print(f"for loopz {i}")


sum = 0
user_number = int(input("enter a number upto 100"))
for i in range (0,user_number+1):
    sum += i
print (f"sum is {sum}")



 # this is for counting the sum of digits such as if 15 = 1+5 =6
user_number = input("enter a number") 
sum = 0
for i in range (len(user_number)):
    sum += int(user_number[i])
print (f"the final sum is:>>> {sum}")



user_name = input("enter your name")
i = 0
while i < len(user_name):
    print (f"{user_name[i]}:{user_name.lower().count(user_name[i])}")
    i += 1



#tells the number of letters specifically
name = input("please enter name")
store = ""
i = 0
while i < len(name):
    if name[i] not in store:
        store += name[i]
        print (f"{name[i]}:{name.lower().count(name[i])}")
    i += 1 



#break and continue
for i in range (1,10):
    if i == 5:
        #continue                       #skips 5 as it sends to for to prints 1-4 and 6-9
        break                            # printss only till 4
    print(f"the new number is: {i}")
    


name = input("please enter name")
store = ""
i = 0
while i < len(name):
    if name[i] not in store:
        store += name[i]
        print (f"{name[i]}:{name.lower().count(name[i])}")
    i += 1 

    

from operator import truediv
import random
chance = 1
guessed_number = int(input("enter a number"))
winning_number = random.randint(1,100)
while guessed_number is not winning_number:
    if guessed_number == winning_number:
        print ("you guessed in first chance")
    elif guessed_number>winning_number:
        print ("your guess is high")
    elif guessed_number<winning_number:
        print ("your guess is low")
    break
chance += 1 
print (f"you guessed in {chance}")

''' 


guess = 1
win = 10
game_over = False
num = int(input("please enter a number"))

while not game_over:
    if num == win:
        print(f"you win and you guessed in {guess} time")
        game_over = True
    else:
        if num < win:
            print ("too low")
        else:
            print ("too high")
    guess += 1
    num = int(input("guesss again"))


