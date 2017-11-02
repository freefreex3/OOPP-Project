import random

def generate_number():
    return random.randint(1,100)

def compare(guessed_number, actual_number):
    result = 'Bingo'
    if guessed_number > actual_number:
        result = 'Too high'
    elif guessed_number < actual_number:
        result = 'Too low'

    return result

# i = 0
# answer = generate_number()
#
# while i <1:
#
#     guessed_number = int(input('Enter a number between 1 to 100: '))
#     result = compare(guessed_number, answer)
#     if  guessed_number==answer:
#         i += 1
#
#
#     print( result)
answer= generate_number()
score=100
while True:
    guessed_number = int(input('Enter a number between 1 to 100: '))
    score -= 1
    result = compare(guessed_number, answer)
    print(result)
    if result == "Bingo":
        print("The number is",answer,"and your score is",score)
        break




