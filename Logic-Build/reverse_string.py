# sample input: python
# expexted output: nohtyp
# find max no.of consecutive 1s in a binary array

name = 'python'
new_name = ''
length = len(name)
i = length-1 #6-1=5
while i>-1:
    new_name += name[i]
    i = i-1

print(new_name)