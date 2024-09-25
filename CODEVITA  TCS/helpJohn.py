n = int(input())
s = input()

i = 0
a = str(n)
j = 0

for i in range(len(s)):

    if s[i] == 'R':
        j = j + 1
        if j >= len(a):  #  j doesn't  out of bounds
            j = len(a) - 1
    elif s[i] == 'L':
        j = j - 1
        if j < 0:  #  j doesn't out of bounds
            j = 0

    elif s[i] == 'T':
        if int(a[j]) <9:
            a = a[:j] + str(int(a[j])+1) + a[j+1:]

    elif s[i] == 'D':
            if int(a[j]) > 0:
                a = a[:j] + str(int(a[j])-1) + a[j+1:]

    elif s[i]=='S':
        if i + 1 < len(s):
            a = list(a)
            a[j], a[int(s[i + 1])-1] = a[int(s[i + 1])-1], a[j]
            a = ''.join(a)
        
print(a)