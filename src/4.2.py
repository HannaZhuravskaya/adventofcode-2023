import re

file = open('./inputs/4.2.txt', 'r')
lines = file.readlines()

cards = {}
sum = 0

for i in range(1, len(lines)+1):
    cards[i] = 0

for line in lines:
    regex = re.findall(r"Card ([0-9 ]+):([0-9 ]+)|([0-9 ]+)", line)
    cardIndex = int(regex[0][0])
    winning = set(regex[0][1].strip().split())
    all = regex[1][2].strip().split()

    numOfWins = 0
    for number in all:
        if number in winning:
            numOfWins += 1

    for i in range(1, numOfWins + 1):
        nextCardIndex = cardIndex + i
        cards[nextCardIndex] = cards[nextCardIndex] + cards[cardIndex] + 1

for value in cards.values():
    sum += 1 + value

print(sum)