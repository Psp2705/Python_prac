# find max and min elements using list looping
# write function to find max and min elements in array 
# input[5,3,9,2,8]
# output: Max:9 Min:2
mylist = [5,3,9,2,8]
max = min = mylist[0]
for i in range(len(mylist)):
    if max < mylist[i]:
        max = mylist[i]

    if min > mylist[i]:
        min = mylist[i]
print('Max: ', max)
print('Min: ', min)