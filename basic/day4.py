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

'''
'''
spaces_problem = "   aar ay     am    a    "
stars = "***********"
print (stars, spaces_problem, stars)
print (stars, spaces_problem.lstrip(),stars)
print (stars, spaces_problem.rstrip(),stars)
print (stars, spaces_problem.strip(),stars)
'''

'''
full_name, char = input("enter your full name with comma").split(",")
space = full_name.strip()
char_count = full_name.count(char)
print (f"your full name is {full_name} and {char} character count is {char_count} ")




#DAY5 ahead
solved_number = spaces_problem.replace(" ","")  #replaces space with non space all. 
print (f"the solve of space problem is:{solved_number}")


replace_example = "kritika is beautiful and is outsstanding"
print(replace_example.find("is"))    #finds in which character there is is.
print(replace_example.replace("is","was"))      #changes all is to was in sentence
print(replace_example.find("a",3))      #finds a only after character 3
print(replace_example.replace("is","was",1))   #replaces is with was first wala only as 1 mentioned
found = replace_example.find("is")
print(replace_example.find("is",found+1))  #finds second is in the sentence





#center() method
example2="python"     #6char
print(example2.center(2+6+2,"*"))      #6 is the number of characters in python and there will be 2 2stars in side..center ma.

full_name = input("enter your full name")
number = len(full_name)
print(full_name.center(5+number+5,"^"))     #centre ma name ani side ma stars.

'''
'''

#string are immutable and assignment operator

example3 = "any"
example3[1] = "N"   #cant do to capital N because it is immutable..ek choti assign garesi change hudaina"
print (example3)


example4 = "any"
print(example4.replace("n","N"))   #this replaces because this is photocopy(newwww)
print(example4)                    #this is original so no changed hence immutable

#example4 = example4 + "body"
example4 += "body"   # adds example4 and body
print (example4)

'''





