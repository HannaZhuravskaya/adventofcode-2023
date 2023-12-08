file = open('./inputs/1.1.txt', 'r')
lines = file.readlines()

sum = 0
cnt = 1

for line in lines:
    num = 0
    for i in range(0, len(line)-1):
        if line[i].isdigit():
            num += int(line[i]) * 10
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            num += int(line[i])
            break
    cnt += 1
    sum += num
print(sum)