s = "is2 sentence4 This1 a3"


ermias=s.split(' ')

for i in range(len(ermias)):
       
        for j in range(len(ermias)-1):
            if int(ermias[j][-1])>int(ermias[j+1][-1]):
                ermias[j],ermias[j+1]=ermias[j+1],ermias[j]

daniel=[]
for i in range(len(ermias)):
    ermiasmulu=ermias[i][:-1]
    daniel.append(ermiasmulu)
dani=" ".join(daniel)
print(dani)




















#  splist=s.split(" ")
       
#         for i in range(len(splist)-1):
#             for j in range(len(splist)-1):
#                 if int(splist[j][-1]) > int(splist[j+1][-1]):
#                     splist[j] ,splist[j+1]=splist[j+1],splist[j]
    
#         for i in range(len(splist)):
#             splist[i] = splist[i][:-1]
    
#         return " ".join(splist)
        