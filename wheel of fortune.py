#desmond justin dylan mervin

import re

sentence = "wheel of fortune"
p = re.compile('\w')
hidden_sentence = p.sub('-', sentence)

while True:
    count = 0
    print('Guess the phrase :', hidden_sentence)
    if hidden_sentence == sentence:
        break
    userGuess = input("Give me a letter: ")
    for i in sentence:
        if userGuess == i:
            hidden_sentence = hidden_sentence[:count] + i + hidden_sentence[count+1:]
        count += 1


print("Yeah, you got it right!")
