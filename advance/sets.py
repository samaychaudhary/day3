'''

intro>> it is an unordered collection of unique items
---> example : set doesnot support indexing
>>> it is usef for remove duplicacy from list
>>>>>> 
'''

sets_any = {"sunday", "monday" , "tuesday"}
any_list = [ 1,2,1,5,9,4,6,8,9,6,2,3]
set_convert = set(any_list)     # converts to list and removes duplicate number
print (set_convert)    

#again to list
list_convert = list(set_convert)
print (list_convert)

one_line_list_set_list = list(set(any_list))             # data lai set ma lagyo ani tei set lai list ma print garyo.
print (one_line_list_set_list)





