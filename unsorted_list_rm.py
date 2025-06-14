# remove duplicates from unsorted list using user define logic 
# write funtion to remove duplicates from unsorted array
# input= [3,2,3,1,2,4]
# outout = [3,2,1,4]

mylist = [3,2,3,1,2,4]
newlist = []

for i in mylist:
    if i not in newlist:
        newlist.append(i)

print(mylist)
print(newlist)