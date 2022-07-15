# for constant list we use tuples
# small bracket is tuples
# ex >>> ("sunday","monday","tuesday")
# tuples are immutable. once created cannot be updates
# no methods like >> append, insert, pop, remove
#tuples are faster than lists



'''tuples only allow these things:
>>count () and index() method
>> len function and slicing in tuples
>> days[0] = "friday"  >> gives error'''

days = ("sunday","monday")
days1 = "sunday", "monday"

print(type(days))    # shows tuples
