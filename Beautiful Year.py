'''
It seems like the year of 2013 came only yesterday. Do you know a curious
fact? The year of 2013 is the first year after the old 1987 with only
distinct digits.

Now you are suggested to solve the following problem: given a year number,
find the minimum year number which is strictly larger than the given one
and has only distinct digits.

Input
The single line contains integer y (1000≤y≤9000) — the year number.

Output
Print a single integer — the minimum year number that is strictly larger
than y and all it's digits are distinct. It is guaranteed that the answer
exists.
'''
# Method 1 : 186 ms
a=input()
n=int(a)+1
while True:
    if len(set(str(n)))==4:
        print(n)
        break
    else:
        n+=1

# Method 2: 248 ms
n=int(input())+1
while True:
    if len(set(str(n)))==4:
        print(n)
        break
    else:
        n+=1

# Method 3: 216 ms
a= int(input())
n=a+1
while True:
    if len(set(str(n)))==4:
        print(n)
        break
    else:
        n+=1

# Method 4: 184 ms
a= int(input())
while True:
    if len(set(str(a+1)))==4:
        print(a+1)
        break
    else:
        a+=1