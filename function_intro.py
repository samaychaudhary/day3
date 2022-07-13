'''guess = 1
win = 10
game_over = False
num = int(input("please enter a number"))

while True:
    if num == win:
        print(f"you win and you guessed in {guess} time")
        break
    else:
        if num < win:
            print ("too low")
            guess += 1
            num = int(input("guess again"))
        else:
            print ("too high")
        guess += 1
        num = int(input("guesss again"))

        #using dry princple here, (do not repeat, like guess += 1 lai tala ek choti lekhda enough and  num wala line pani.)

#FUNCTION

def function_name(like):
    print (f"krtika deo  {like}")


# function calling  with arguement

print (function_name(", hello"))

name = input("Your name please:-->")
age = input("Your age please:-->")

def any(name,age):
    print(f"welcome {name} and your age is {age}")

print(any(name,age))



#24 % 2 == 0 even ho

number = int(input("enter a number"))
def any(number):
    if number % 2 == 0:                                    
         return "given number is even"                   
    else:                                           
        return "given number is odd"      
my_value=any(number)                                           # number ma mathi ko output stored cha that gets stored to my_value. 
print (my_value)


number = int(input("enter a number"))
def any(number):
    if number % 2 == 0:                                    
         return "given number is even"     
    return "given number is odd"              
        
my_value=any(number)                                           # number ma mathi ko output stored cha that gets stored to my_value. 
print (my_value)



# making it kiss ( short and simple stupid)
number = int(input("enter a number"))
def any(number):
    return number % 2 ==0
my_value=any(number)                                           # number ma mathi ko output stored cha that gets stored to my_value. 
print (my_value)



number = (input("enter a number"))
print (number[-1 :: -1])

#baaki cha



number1 = int(input("enter number"))
number2 = int(input("enter another number"))
def greatlow(any1,any2):
    if any1>any2:
        return(f"{any1} is greater than {any2}")
    else:
        return(f"{any2} is greater than {any1}")
my_value = greatlow(number1,number2)
print (my_value)


number1,number2,number3 = (input("enter three number")).split(",")
def greatlow(any1,any2,any3):
    if any1>any2 and any1>any3:
        return(f"{any1} is greatest")
    elif any2>any1 and any2>any3:
        return(f"{any2} is greatest")
    elif any3>any1 and any3>any2:
        return(f"{any3} is greatest")
    else:
        return("bhagg")
my_value = greatlow(int(number1), int(number2), int(number3))
print (my_value)

'''
first, second, third = input("enter three numbers").split(",")
def greater(a,b):
    if a>b:
        return f"{a}>{b}"
    else:
        return f"{b}>{a}"

def greatest(a,b,c):
    greater_of_two_num = greater(a,b)
    return greater(greater_of_two_num)

#def greatest(a,b,c):
# return greater(greater(a,b),c)
    
anything = greatest(int(first),int(second),int(third))
print(anything)






