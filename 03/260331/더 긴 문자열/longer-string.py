sentence = input().split()

if len(sentence[0]) > len(sentence[1]):
    print(sentence[0], end=" ")
    print(len(sentence[0]))

elif len(sentence[0]) < len(sentence[1]):
    print(sentence[1], end=" ")
    print(len(sentence[1]))

elif len(sentence[0]) == len(sentence[1]):
    print("same")