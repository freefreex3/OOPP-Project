date = input("Please enter the date:")
psi = []
psivalues1 =input("Please enter the psi values for the north:")
psivalues2 =input("Please enter the psi values for the south:")
psivalues3 =input("Please enter the psi values for the east:")
psivalues4 =input("Please enter the psi values for the west:")

psi.append(psivalues1)
psi.append(psivalues2)
psi.append(psivalues3)
psi.append(psivalues4)

psireadings = {date:psi
               }





print ( "The date is:",date)
print ("The maximum psi reading is",max(psi))
print ("The minimum psi reading is",min(psi))
print("The psi readings for each regions ,north,south,east and west respectively",psi)
