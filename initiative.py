
from operator import itemgetter
def printInitiative(initiativeList):
    print('\n\nInicjatywa:')
    for i in initiativeList:
        print(i["name"], ":", i["init"])

def extendInitiativeList(initiativeList):
    name = input("nazwa: ")
    initValue = int(input("Inicjatywa: "))
    player = {
        "name" : name,
        "init" : initValue
    }
    initiativeList.append(player)
    initiative.sort(reverse=True, key=itemgetter("init"))
    return initiativeList

def removeItemFromList(initiativeList):
    name = input("Kogo wyjebac: ")
    for i in initiativeList:
        if i["name"] == name:
            initiativeList.remove(i)
    return initiativeList


participants = int(input("Ilosc walczacych: "))
initiative = []

for i in range(participants): 
    print("--", i+1, "--")
    initiative = extendInitiativeList(initiative)

#petla programu
print( "<h> - wyswietla pomoc\n<d> - dodaje uczestnika walki\n<r> - usuwa uczestnika walki\n<p> - wypisuje liste inicjatywy\n<q> - wyjdz")
while True:
    action = input("Akcja (h/d/r/p/q):" )
    if action == 'h':
        print( "<h> - wyswietla pomoc\n<d> - dodaje uczestnika walki\n<r> - usuwa uczestnika walki\n<p> - wypisuje liste inicjatywy\n<q> - wyjdz")
    elif action == 'd':
        initiative = extendInitiativeList(initiative)
    elif action == 'r':
        initiative = removeItemFromList(initiative)
    elif action == 'p':
        printInitiative(initiative)
    elif action == 'q':
        choice = input("Jestes pewny ze chcesz wyjsc? TAK/cokolwiek: ")
        if choice == "TAK":
            break
    else:
        print("aby otrzymac pomoc wpisz <h>")



        


