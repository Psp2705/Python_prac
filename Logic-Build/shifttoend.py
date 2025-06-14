# shift zero's to end of list
# given array move all zeros to end without changing order of non-zero elements

# input [0,1,0,3,12]
# output [1,3,12,0,0]

mylist = [0,1,0,3,12]
for i in range(len(mylist)): # i=0
    if mylist[i]==0:
        mylist.append(0)
        del mylist[i]


print(mylist)