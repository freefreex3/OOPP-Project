# highestscore = 0
# correctans=["C","D","B","A","B","D","A","C","D","C"]
# givenans= []
#
# for i in range (10):
#     msg = "Enter ans #" + str(i+1)
#     ans = input(msg)
#     givenans.append(ans)
# count = 0
# for s in range (10):
#     if givenans[i] == correctans[i]
#         count += 1
# mark = 0
# if count > mark:
#     mark=count
#
# print(highestscore)
# print(correctans)

correctans=["C","D","B","A","B","D","A","C","D","C"]
mark = 0

while True :
    studentattempt = []
    print("Please enter your Review Exercise answer")
    for n in range(10): #Step 1 - ask for given answer
        studentattempt.append(input("MCQ #%d:" %(n+1)))

    count = 0
    for i in range(10): #Step 2 - compare the answer
        if correctans[i] == studentattempt[i]:
            count += 1 #count for num of correct ans

    if count > mark : #is it highest score.if yes,store!
        mark = count

    print("You have %d correct answer and %d wrong answer" %(count,10-count))


    tryagain = input ("Do you want to try again? (Y/N)")
    # Step 3 - go back to step 1 of re-attempt,otherwise quit!
    if tryagain=="Y" or tryagain=="y":
        continue
    else:
        break

print("Your mark for Review Exercise is %.1f" %(mark/2))
print("Review Exercise Answers:")
print(correctans)









