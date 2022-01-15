def deplacement(origin, destination, disc):
  

    origin.remove(disc)
    destination.append(disc)


def Tower(disques, origin, destination, help):
  if len(disques) == 1 :
    deplacement(origin,destination,disques[0])
    return
  
  if len(disques) == 2 :

    deplacement(origin,help,disques[1])
    
    deplacement(origin, destination,disques[0])
    
    deplacement(help, destination,disques[1])

    return 
  
  Tower(disques[1:], origin, help, destination)
  Tower(disques[0:1], origin, destination, help)
  Tower(disques[1:], help, destination, origin)

disques = ["d1","d2","d3","d4","d5","d6","d7"]
T1 =disques[:]
T2=[]
T3=[]

print("Départ")
print("T1 \t",T1,"T2 \t",T2,"T3 \t",T3)
print("----"*len(disques)*3)

Tower(disques, T1,T2,T3)

print("FIN")
print("T1 \t",T1,"T2 \t",T2,"T3 \t",T3)
print("----"*len(disques)*3)
