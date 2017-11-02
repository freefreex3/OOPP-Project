import datetime

now = datetime.datetime.now()

print(now)

enrolmentDate = str(now.day) + "-" +str(now.month) +"-"+ str(now.year)

print(enrolmentDate)
