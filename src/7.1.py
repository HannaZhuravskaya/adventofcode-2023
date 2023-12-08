from functools import cmp_to_key

file = open('./inputs/7.1.txt', 'r')
lines = file.readlines()

hands = {}

for line in lines:
    handWithBid = line.split()
    hands[handWithBid[0]] = int(handWithBid[1])

cardMappings = {'A' : 12, 'K' : 11, 'Q' : 10, 'J':9, 'T':8, '9':7, 
                '8':6, '7':5, '6':4, '5':3, '4':2, '3':1,  '2':0}

def getHandType(hand):
    combination = [0 for i in range(0, 13)]

    for card in hand:
        combination[cardMappings[card]] += 1

    combination = sorted(combination, reverse=True)

    if combination[0] == 5:
        return 7
    elif combination[0] == 4:
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