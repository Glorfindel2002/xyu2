# basement
P = 27
# module
M = pow(2, 61) - 1


def poly_hash(s):
    h = 0
    for c in s:
        h = ((h * P) % M + ord(c) - ord('a') + 1) % M
    return h
######################################


def karp(s, w):
    ans = []
    n = len(s)
    m = len(w)
    hashS = poly_hash(s[0:m])
    hashW = poly_hash(w)
    pm = pow(P, m) % M
    for i in range(n - m + 1):
        if hashS == hashW:
            ans.append(i)
        if i < n - m:
            hashS = (P * hashS - pm * poly_hash(s[i]) + poly_hash(s[i + m])) % M
    
    if len(ans) == 0:
        ans.append(-1)
    return ans
##################################################################################


w = input()
s = input()

ans = karp(s, w)
print(*ans)
