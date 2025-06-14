# find second largesy ele,emt in array
# initialize 2 var to store largesy amd 2mdlargest element 
# and iterate through array
# input [7,3,9,2,8]
# outpt second largest: 8

mylist = [7,3,9,2,8]
mylist.sort()
print('Mylist= ',mylist)

print('Largest= ',mylist[-1])
print('Second Largest= ',mylist[-2])