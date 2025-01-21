import sys

ongoing_tasks = list()
completed_tasks = list()

def createitem():
   todo=input("what is on your to do list?")
   ongoing_tasks.append(todo)

def removeitem():
    remitem=int(input("what item do you want to remove?"))

    if remitem > len(ongoing_tasks):
        print("cannot do that")
    else:
        removed = ongoing_tasks.pop(remitem - 1)
        completed_tasks.append(removed)

def viewall():
    print("")
    for i in range(len(ongoing_tasks)):
        print("Item " + str(i + 1) + ": " + ongoing_tasks[i])
    print("")

def viewallcomp():
    print("")
    for i in range(len(completed_tasks)):
        print("Item " + str(i + 1) + ": " + completed_tasks[i])
    print("")

def exit():
    sys.exit()

# print(datetime.datetime.now())

while True:
    print("press 1 to create\npress 2 to remove a to do\npress 3 to view all\npress 4 to view all completed \npress 5 to exit menu")
    choise=int(input("what do you click?"))
    if choise == 1:
        createitem()
    elif choise == 2:
        removeitem()
    elif choise == 3:
        viewall()
    elif choise == 4:
        viewallcomp()
    elif choise == 5:
        exit()
