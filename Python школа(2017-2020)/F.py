
map = input()
#map = 'LLBLRRBRL'
ans = map.count('B')
map = map.replace('B', '')+' '
 
count = 0
side = 'L'
# 0 - left
 
i = 0
# print(map)
while i < len(map):
    # print(i, map[i:i+2], side+side, end=' ')
 
    if (map[i:i+2] == 'L ' or map[i:i+2] == ' ') and side == 'L':
        count += 1
        break
    if (map[i:i+2] == 'R ' or map[i:i+2] == ' ') and side == 'R':
        break
 
    if map[i:i+2] == side+side:
        count += 1
        if side == 'L':
            side = 'R'
        else:
            side = 'L'
        i += 2
    elif map[i] == side:
        count += 1
        i += 1
    else:
        i += 1
 
print(ans + count)
