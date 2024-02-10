'''
Ternary numeric notation is quite popular in Berland.
To telegraph the ternary number the Borze alphabet is used.
Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--».
You are to decode the Borze code, i.e. to find out the ternary number
given its representation in Borze alphabet.

Input
The first line contains a number in Borze code. The length of the string
is between 1 and 200 characters. It's guaranteed that the given string
is a valid Borze code of some ternary number (this number can have
leading zeroes).

Output
Output the decoded ternary number. It can have leading zeroes.
'''
# Method 1: Execution time: 218 ms

a=input()
s=''
while a!='':
    if a[0]=='.':
        s+='0'
        a=a[1::]
    elif a[0]=='-':
        if a[1]=='.':
            s+='1'
        elif a[1]=='-':
            s+='2'
        a=a[2::]
print(s)

# Method 2:
a=input()
s=''
while a!='':
    if a[0]=='.':
        s+='0'
        a=a[1::]
    elif a[:2]=='-.':
        s+='1'
        a = a[2::]
    elif a[:2]=='--':
        s+='2'
        a = a[2::]

print(s)