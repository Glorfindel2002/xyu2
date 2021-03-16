# basement
P = 2
# module
M = (1 << 61) - 1

def poly_hash(s):
    h = 0
    for c in s:
        h = (h * P + ord(c)) % M
    return h
######################################
