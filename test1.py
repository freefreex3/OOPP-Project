vehiclelist={"SJA123T":["Tan Mei Mei","13 Sep 2008"],
             "SA007":["James","07 Jul 2007"],
             "SA008":["Mary","07 Jul 2008"]
             }


for key in vehiclelist:
    record=vehiclelist[key]
    print(key,end="")


    for i in range(20-len(key)):
                print(" ",end="")
    print(record[0],end="")
    for i in range(15-len(record[0])):
        print(" ",end="")
    print(record[1])
