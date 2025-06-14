# count and display max consecutive ones
# find max no of consecutive in a binary
# input [1,1,0,1,1,1,0,1,1,1,1]
# output 4


mylist = [1,1,0,1,1,1,0,1,1,1,1]
newlist = []
count = 0
for i in mylist:
    if i ==1:
        count += 1
    else:
        newlist.append(count)
        count = 0

newlist.append(count)
print(newlist)
print('Max no: ', newlist[2])
