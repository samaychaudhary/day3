'''
intro---> it is a ordered collection of items
ex: number=[1,2,3,4]
words, mixed


from pickle import FALSE


list_of_numbers = [1,2,3,4]
list_of_nepali_names = ["kritika", "aryama", "samay", "rushav", "maharshi"]
list_of_even_numbers = [2,4,6]
list_of_odd_numbers = [1,3,5]

mixed = ["one",2.0,3,"four"]

for i in mixed:
    print (f"{type(i)}\n")
print (list_of_odd_numbers[1:2])
list_of_odd_numbers[2]=False
print (list_of_odd_numbers[2])

print (type(mixed))



# 2) add data to list--->>>>> append() method     #append le last ma insert garcha list ko 
list_of_numbers.append (6)
list_of_numbers.insert(2,11)           # 2 is position ..>> 2nd position ma 11 aucha tesma (1,2,11,3,4,6)

print (list_of_numbers)


#3) remove or delete from list

fruits1 = ["apple","mango","banana"]
fruits2 = ["grapes","watermelon","guava"]

#fruits1.pop()       #removes the last from list  # by default last ho 
#print (fruits1)

fruits1.pop(0)
print (fruits1)              # prints mango not banana because mathi banana hataisakyo.
popped_item = fruits1.pop(0)
print (popped_item)



#4) in keyboard in list

if "apple" in fruits1:
    print ("present")
else:
    print ("not present")



print(fruits2.count("grapes"))
fruits2.sort()
print (fruits2)
fruits2.reverse()
print (fruits2)
fruits2.clear()
print (fruits2)



# sort and sorted
# sort >>> changes the the original thing and never goes back
# sorted >>> changes the original thing temporarily and does not change over all , it is used to save in another variable


# is vs equal --> comparison

fruits5 = ["apple","banana","mango"]
fruits6 = ["apple","banana","mango"]

print (fruits5 == fruits6)    # check for same value as well as num
print (fruits5 is fruits6)     # check for the location/address of object in memory i.e. RAM



def give_me_list(num):
    my_list = []
    for i in range (0,num+1):
        my_list.append(i)
    return my_list

mero_list_diyo_hurray = give_me_list(10)
print (mero_list_diyo_hurray)


number_given = int(input("enter a number between 0 to 20"))
def square(num):
    my_list = []
    for i in range (0,num+1):
        my_list.append(i**2)
    return my_list

mero_list = square(number_given)
print (mero_list)



given_list = [0,1,2,3,4,5,6,7,8,9,10]

def rev_list (any_list):
    reversed_vako_list = any_list[-1::-1]
    return reversed_vako_list 

ok = rev_list(given_list)
print (ok)


given_list = [0,1,2,3,4,5,6,7,8,9,10]

def rev_list (any_list):
    reversed_vako_list = any_list[-1::-1]
    return reversed_vako_list 

ok = rev_list(given_list)
print (ok)



def rev_list (any_list):  
    any_list.reverse()
    return any_list

ok = rev_list(given_list)
print (ok)





given_list = [0,1,2,3,4,5,6,7,8,9,10]


def pop (any_list):
    reversed_list = []
    for item in any_list:
        popped_item = any_list.pop()
        reversed_list.append(popped_item)
    return reversed_list

ok = pop(given_list)
print (ok)


name_lists = ["aryama","kritika","rushav","samay",'maharshi']

def reverse(any_list):
    reversed_list = []
    for item in any_list: 
        reversed_list.append(item[-1::-1])
    return (reversed_list)

ok = reverse(name_lists)
print (ok)

'''

num = int(input("enter a number"))
generated_list = list(range(0,num+1))
count = 0 

def oddeven(number_list):
    number_list_odd = []
    number_list_even = []
    for i in number_list:
        if i % 2 == 0:
            number_list_even.append(i)
        else:
            number_list_odd.append(i)
    return [number_list_even, number_list_odd]

ok = oddeven(generated_list)
print (ok)

returned_values = oddeven(generated_list)
print (returned_values)


def list_counter (mixed_lists):
    count = 0
    for items in mixed_lists:
        type_of_elements = type(items)
        if type_of_elements == list:
            count += 1
    return count

ok = list_counter(returned_values)
print (ok)


