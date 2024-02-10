'''
PROBLEM:
A guy named Vasya attends the final grade of a high school.
One day Vasya decided to watch a match of his favorite hockey team.
And, as the boy loves hockey very much, even more than physics,
he forgot to do the homework. Specifically, he forgot to complete his
physics tasks. Next day the teacher got very angry at Vasya and decided
to teach him a lesson. He gave the lazy student a seemingly easy task:
You are given an idle body in space and the forces that affect it.
The body can be considered as a material point with coordinates (0; 0; 0).
Vasya had only to answer whether it is in equilibrium.
"Piece of cake" — thought Vasya, we need only to check if the sum of
all vectors is equal to 0. So, Vasya began to solve the problem.
But later it turned out that there can be lots and lots of these forces,
and Vasya can not cope without your help. Help him. Write a program
that determines whether a body is idle or is moving by the given vectors
of forces.

Input
The first line contains a positive integer n (1≤n≤100),
then follow n lines containing three integers each:
the xi coordinate, the yi coordinate and the zi coordinate of the force vector,
applied to the body (-100≤xi,yi,zi≤100).

Output
Print the word "YES" if the body is in equilibrium,
or the word "NO" if it is not.

'''
# Method 1 : 154 ms
xs, ys, zs = 0, 0, 0
for x in range(int(input())):
    v = list(map(int, input().split()))
    xs += v[0]
    ys += v[1]
    zs += v[2]
if xs == 0 and ys == 0 and zs == 0:
    print('YES')
else:
    print('NO')

# Method 2 : 186 ms
x,y,z=0,0,0
for q in range(int(input())):
    a=tuple(map(int,input().split()))
    x+=a[0]
    y+=a[1]
    z+=a[2]
if x==0 and y==0 and z==0:
    print('YES')
else:
    print('NO')

# Method 3 : 184 ms
x1,y1,z1=0,0,0  #It's the same as method 1, but idk why it took more time
for x in range(int(input())):
    a=list(map(int,input().split()))
    x1+=a[0]
    y1+=a[1]
    z1+=a[2]
if x1==0 and y1==0 and z1==0:
    print('YES')
else:
    print('NO')

