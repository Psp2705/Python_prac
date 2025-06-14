# remove duplicates from string
# find max no of consecutive is in a binary array
# input: programming
# output: progamin

name = 'programming'
new_name = ''
for i in range(len(name)):
    if name[i] not in new_name:
        new_name += name[i]

print(name)  
print(new_name)