# basement
P = 91
# module
M = 100
# table size
TABLE_SIZE = 10


def poly_hash(s):
    h = 0
    for c in s:
        h = (h * P + ord(c)) % M
    return h
######################################


def get_pos(key):
    h = poly_hash(key)
    return (h % TABLE_SIZE, h)
##############################


# unit = [hash, key, value]


def insert(table, key, value):
    pos, h = get_pos(key)
    for unit in table[pos]:
        if unit[1] == key:
            unit[2] = str(value)
            return
    new_unit = [h, key, value]
    table[pos].append(new_unit)
    return
###############################


def search(table, key):
    pos, h = get_pos(key)
    for unit in table[pos]:
        if unit[1] == key:
            return unit[2]
    return 'KeyError'
###########################


def remove(table, key):
    pos, h = get_pos(key)
    for i, unit in enumerate(table[pos]):
        if unit[1] == key:
            value = unit[2]
            table[pos].pop(i)
            return value
    return 'KeyError'
##########################################


table = [[] for _ in range(TABLE_SIZE)]
count = int(input())

for i in range(count):
    s = input()
    key = s[0:s.find(' ')]
    value = s[s.find(' ')+1:]
    insert(table, key, value)

for i in range(TABLE_SIZE):
    if len(table[i]) != 0:
        print(i)
        for j in range(len(table[i])):
            print(*table[i][j])
#########################################
