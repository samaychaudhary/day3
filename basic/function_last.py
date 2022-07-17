'''def give_Me(f_name, age, l_name= "apple"):
    return f"your full name is {f_name} {l_name} and your age is {age}"

personal_details = give_Me("aryama",21)        #non default arguement follows default arguement
print (personal_details)





def give_Me(f_name, age, l_name= "apple"):
    return f"your full name is {f_name} {l_name} and your age is {age}"

personal_details = give_Me(age=21, l_name="deo", f_name="samay")        #non default arguement follows default arguement
print (personal_details)'


# global parameter vs local parameter

def any_function():
    any_value = 7           #local variable 
    print (any_value)            # this any_value only works in this function range
 
def aarko_function():
    print (any_value)             # any_value ony works in above function. 
'''
any_value = 10      #global variable           # this is global
def any_function ():
    global any_value  # now tala ko is global... 
    any_value = 11                     
    #any_value = 7 local variable
    print (any_value)

print (any_function())