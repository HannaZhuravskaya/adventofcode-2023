_end = '_end_'

def make_trie(words, wordsEnds):
    root = dict()
    for i in range(0, len(words)):
        current_dict = root
        for letter in words[i]:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = wordsEnds[i]
    return root


def in_trie(root, word, start):
    curr = root
    for i in range(start, len(word)):
        if word[i] in curr:
            curr = curr[word[i]]
            if _end in curr:
                return (True, start + 1, curr[_end])
        else:
            return (False, start + 1, None)
    return (False, start + 1, None)

file = open('./inputs/1.2.txt', 'r')
lines = file.readlines()

root = make_trie(['one','two','three','four','five','six','seven','eight','nine'], [1, 2, 3, 4, 5, 6, 7, 8, 9])

sum = 0

for line in lines:
    digits = []
    curr = root
    i = 0
    while i < len(line):
        if line[i].isdigit():
            digits.append(int(line[i]))
            i += 1
        else:
            (inTrie, newI, digit) = in_trie(root, line, i) 
            if inTrie == True:
                digits.append(digit)
            i = newI

    num = digits[0] * 10 + digits[len(digits)-1]
    sum += num    

print(sum)