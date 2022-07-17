# for constant list we use tuples
# small bracket is tuples
# ex >>> ("sunday","monday","tuesday")
# tuples are immutable. once created cannot be updates
# no methods like >> append, insert, pop, remove
#tuples are faster than lists



'''tuples only allow these things:
>>count () and index() method
>> len function and slicing in tuples
>> days[0] = "friday"  >> gives error

days = ("sunday","monday")
days1 = "sunday", "monday"

print(type(days))    # shows tuples
#days[1] = "tuesday"
print (days[1])
print (len(days))

# tuple unpacking (js object de-structuring) same value:
day1, day2, day3 = days
print (day2)


# function returning two values

def calculator(num1, num2):
    sum = num1+num2
    multiply = num1*num2
    return sum, multiply

returned_value = calculator(4,5)
print (f"the returned value is : {returned_value}")
print (f"the type of returned value is :{type(returned_value)}")

sum , multiply = returned_value        #this is unpacking for multiply. 
print (multiply)


# list inside tuples

tuple_a = (1,2,3,[4,5,6],7,8,9)
print (tuple_a[3])
print (type(tuple_a[3]))
#tuple_a[3] = "kritika"     # cannot be done 

tuple_a[3][1] = "kritika"    # [3]denotes that list mathi and [1] tesko bhitra 5 lai kritika lai replace garne.
print (tuple_a)
'''


'''
tuple_a = (1,2,3,[4,5,6],7,8,9)

searched_value = "sth"
left_pointer  = 0
right_pointer = len(tuple_a)-1
mid_pointer = (left_pointer+right_pointer)/2
if value<mid_pointer: 
    right_pointer = mid_pointer        # esma aba mid pointer ko value right banyo so right pointer is  5 aba. 


'''




tuple_a = (1,2,3,[4,5,6],7,8,9)
tuple_b = (1,2,3,4,5,6,7,8,9)
tuple_a[3][1] = "kritika"
print (tuple_a)
print (max(tuple_b))
print (min(tuple_b))
print (sum(tuple_b))

# more about tuples
# creating new tuple from range function as like list

new_tuples = tuple(range(1,11))
print (new_tuples)

create_list_from_tuples = list(new_tuples)
print (f"{create_list_from_tuples} and its type is: {type(create_list_from_tuples)}")   #gets list from tuples

create_list_from_tuples = str(new_tuples)
print (f"the string is: {create_list_from_tuples} and its type is; {type(create_list_from_tuples)}")   # this whole tuple is a string. not sinle item





