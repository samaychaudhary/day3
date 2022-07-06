#first_name,second_name = input ("please provide your full name space separated").split(",")
#name_type = type (first_name)
#print ("your ful name is--->" + first_name+" "+second_name)
#print (name_type)
#print ("sam")

'''
first_number, second_number, third_number =input ("please provide three numbers comma separated").split(",")
sum = int(first_number) + int(second_number) + int(third_number)
average = (sum/3)
print ("the average of three number is", average)

#string indexing

name = "language"
          #012345678
          #-7 -6 -5 -4 -3 -2 -1 

print (name[3])  #prints g

print (name[3:5])  #prints gu not gua

print (name[1:7:2])  #prints 1 to 7 all in step 2 

print (name[::])   #prints all

print (name[::-1])    #prints reverse

print (name[-1::-1])  #prints reverse from -1 to -1 (all)

print (len(name))    #prints number of alphabets





example = "LeArN pYtHon"
print(example.lower())      #all smallcase
print(example.upper())      #all uppercase
print(example.title())      #title way
print(example.count("p"))   #counts how many p are there



name = input("enter your full name")
print(name.count("a"))
print(name.count(" a"))  #0 a because this is space a 
print(name.lower().count("s"))



name = input("enter your full name")
character = input("enter character you want")
print (name.count(character))     



fullname,char = input("full name and char..").split(",")
print("your fullname is:",fullname,"and your character count is",fullname.count(char))


fullname,char = input("full name and char..").split(",")
char_count = fullname.lower().count(char)
#print("your fullname is: "+fullname+
print ("your fullname is {} and {} character count is {}".format(fullname,char,char_count)) #python3
print (f"your full name is {fullname} and {char} character count is {char_count}")  #python3.6

#solved problem with spaces: lstrip(), rstrip(), strip()   # lstrip le left side bata space hataucha, strip le both side, only space

spaces_problem = "   aarayama    "
stars = "***********"
print (stars, spaces_problem, stars)
print (stars, spaces_problem.lstrip(),stars)
print (stars, spaces_problem.rstrip(),stars)
print (stars, spaces_problem.strip(),stars)

'''

full_name, char = input("enter your full name with comma").split(",")
space = full_name.strip()
char_count = full_name.count(char)
print (f"your full name is {full_name} and {char} character count is {char_count} ")


