guess = 1
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


