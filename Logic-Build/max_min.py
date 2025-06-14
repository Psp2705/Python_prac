# find max and min elements using list slicing
# write function to find max and min elements in array 
# input[5,3,9,2,8]
# output: Max:9 Min:2

mylist = [5,3,9,2,8]
mylist.sort()
print(mylist)
print('maximum: ', mylist[-1])
print('Minimum: ', mylist[0])