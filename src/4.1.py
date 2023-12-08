import re

file = open('./inputs/4.1.txt', 'r')
lines = file.readlines()

sum = 0

for line in lines:
    regex = re.findall(r"Card [0-9 ]+:([0-9 ]+)|([0-9 ]+)", line)
    winning = set(regex[0][0].strip().split())
    all = regex[1][1].strip().split()

    score = 0

    for number in all:
        if number in winning:
            if score == 0:
                score  = 1
            else:
                score *= 2
    sum += score
 
print(sum)
