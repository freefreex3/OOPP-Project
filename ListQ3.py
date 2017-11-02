examResults = {"Jane":[75,80,85],
               "John":[60,68,74],
               'Jerome':[81,63,77],
               "Jason":[55,76,67],
               "Jessica":[62,45,68],
               "Joanne":[52,47,51]}

name = input("Enter student name:")
studentResult = examResults.get(name,"student does not exist") #does not exist - provides a deafult message if value entered is invalid

print("Results of",name)
print("=================================")
print("English",studentResult[0])
print("Math",studentResult[1])
print("Science",studentResult[2])



engresults = 0
mathresults = 0
sciresults =0

print("===============================")
for key in examResults:
    average = (examResults[key][0] + examResults[key][1]
                + examResults[key][2])/3
    print("Average marks of",key,":%.2f" %average)

    engresults += examResults[key][0]
    mathresults += examResults[key][1]
    sciresults += examResults[key][2]


engresults = engresults/len(examResults)
mathresults = mathresults/len(examResults)
sciresults = sciresults/len(examResults)
print("====================================")
print("Average results for English:%.2f" %engresults)
print("Average results for Math:%.2f" %mathresults)
print("Average results for Science:%.2f" %sciresults)
