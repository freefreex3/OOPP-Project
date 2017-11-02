import random




def quiz(num1, num2, operation):
    # implement the logic for quiz function here
    # operation parameter can accept '+' and '-' only
    if operation == "-":
        answer = int(input("What is the difference of " + str(num1)+ " and " +str(num2) + "?"))
    elif operation == "+":
        answer = int(input("What is the sum of " + str(num1) + " and " + str(num2)+"?"))
    elif operation == "*":
        answer = int(input("What is the product of " + str(num1) + " times " + str(num2) + "?"))
    if operation == "+" and answer == num1 + num2:
        print("Congratulations! You have gained 1 point!")
        return 1
    elif operation == "-" and answer == num1 - num2:
        print("Congratulations! You have gained 2 points!")
        return 2
    elif operation == "*" and answer == num1 * num2:
        print("Congratulations! You have gained 5 points!")
        return 5
    else:
        print("Sorry,your answer is incorrect")
        return 0

def main():
    times = int(input("Please enter the amount of times you wanna play:"))
    for i in range(1,times+1):

        x = random.randint(0,100)
        y = random.randint(0,100)
        score1 = quiz(x,y,'-')
        x = random.randint(0,100)
        y = random.randint(0,100)
        score2 = quiz(x,y,'+')
        x = random.randint(0,100)
        y = random.randint(0,100)
        score3 = quiz(x,y,'*')
        totalscore=score1+score2+score3
        print('You have earned', totalscore, 'points')
        brea

main()
