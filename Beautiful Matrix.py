'''
You've got a 5×5 matrix, consisting of 24 zeroes and a single number one. 
Let's index the matrix rows by numbers from 1 to 5 from top to bottom, 
let's index the matrix columns by numbers from 1 to 5 from left to right. 
In one move, you are allowed to apply one of the two following 
transformations to the matrix:

Swap two neighboring matrix rows, that is, rows with indexes i and i+1 
for some integer i (1≤i<5).
Swap two neighboring matrix columns, that is, columns with indexes j 
and j+1 for some integer j (1≤j<5).
You think that a matrix looks beautiful, if the single number one of the 
matrix is located in its middle (in the cell that is on the intersection 
of the third row and the third column). 
Count the minimum number of moves needed to make the matrix beautiful.

Input
The input consists of five lines, each line contains five integers: 
the j-th integer in the i-th line of the input represents the element 
of the matrix that is located on the intersection of the i-th row and 
the j-th column. It is guaranteed that the matrix consists of 24 zeroes 
and a single number one.

Output
Print a single integer — the minimum number of moves needed to make 
the matrix beautiful.
'''



# Method 1 : Max time: 186 ms

r={}
r['_2'], r['_1'], r['0'], r['1'], r['2'] = input().split(),input().split(),input().split(),input().split(), input().split()
steps=0
def left_right_steps(r0,rn):
    global steps
    steps += rn
    if r0.index('1') in [0, 4]:
        steps += 2
    elif r0.index('1') in [1, 3]:
        steps += 1
for x in r:
    if '1' in r[x]:
        left_right_steps(r[x],int(x[-1]))
print(steps)

# Method 2: max time: 154 ms

r0=list(map(int,input().split()))
r1=list(map(int,input().split()))
r2=list(map(int,input().split()))
r3=list(map(int,input().split()))
r4=list(map(int,input().split()))
s=0
m=[r0,r1,r2,r3,r4]
for x in range(5):
    if 1 in m[x]:
        i1=[x,m[x].index(1)]
s=abs(2-i1[0])+abs(2-i1[1])
print(s)


# Method 3: 154 ms

for x in range(-2,3):
    l=tuple(input().split())
    if '1' in l:
        steps=abs(x)+abs(2-l.index('1'))
        break
print(steps)


# Method 4: 184 ms

for x in range(-2,3):
    l=tuple(input())
    if '1' in l:
        steps=abs(x)+abs(2-(l.index('1')//2))
        break
print(steps)

