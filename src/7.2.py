from functools import cmp_to_key

file = open('./inputs/7.2.txt', 'r')
lines = file.readlines()

hands = {}

for line in lines:
    handWithBid = line.split()
    hands[handWithBid[0]] = int(handWithBid[1])

cardMappings = {'A' : 12, 'K' : 11, 'Q' : 10, 'T':9, '9':8, 
                '8':7, '7':6, '6':5, '5':4, '4':3, '3':2,  '2':1, 'J':0}

def getHandType(hand):
    combination = [0 for i in range(0, 13)]

    for card in hand:
        combination[cardMappings[card]] += 1

    jokers = combination[cardMappings['J']]
    combination[cardMappings['J']] = 0

    combination = sorted(combination, reverse=True)

    while jokers > 0:
        if combination[0] < 5:
            combination[0] += 1
        else:
            combination[1] += 1
        jokers -= 1

    if combination[0] >= 5:
        return 7
    elif combination[0] >= 4:
        return 6
    elif combination[0] == 3 and combination[1] == 2:
        return 5
    elif combination[0] == 3:
        return 4
    elif combination[0] == 2 and combination[1] == 2:
        return 3
    elif combination[0] == 2:
        return 2
    else:
        return 1

def compare(hand1, hand2):
    handType1 = getHandType(hand1)
    handType2 = getHandType(hand2)

    if handType1 > handType2:
        return 1
    
    if handType1 < handType2:
        return -1

    if handType1 != handType2:
        return hand1 > hand2
    
    for i in range(0, 5):
        handScore1 = cardMappings[hand1[i]]
        handScore2 = cardMappings[hand2[i]]
        if handScore1 > handScore2:
            return 1
        elif handScore1 < handScore2:
            return -1
   
orderdHands = sorted(hands.keys(), key=cmp_to_key(compare))

answer = 0

for i in range(0, len(orderdHands)):
    answer += hands[orderdHands[i]] * (i+1)

print(answer)