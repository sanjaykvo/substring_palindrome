""" This program will create the substring of the string and check the substring or not. if the substring is a
palindrome then it will print the substring if anyone of the substring is not a palindrome it will print invalid
input. """


def pal(st):
    if st == st[::-1]:
        return 1


def l(s):
    l1 = []
    l1[:0] = s
    return l1


def brea(k):
    i = 0
    c = ''
    for i in range(0, len(k)):
        c = c + k[i]
        if pal(c) == 1 and i > 0:
            alp.append(c)
            break
    return i


s = str(input())
k = l(s)
rk = k

alp = []

for j in range(len(k)):
    i = brea(k)
    k = k[i + 1:len(k)]
    if i == len(k):
        break
if len(alp) < 1 or len(alp) > len(k):
    print('invalid input')

else:

    for i in range(len(alp)):
        print(alp[i], end=' ')


