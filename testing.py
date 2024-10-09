def helloworld():
    print("hello, world")

def pyramid():   
    t = 0
    for i in range(5):
        t += 1
        for i in range(t):
            print("x", end = "")
        print()
def listTrial():
    boxoffour = [["X","X","X","X","X","X","X","X","X"],
                 ["X","X","X","X","X","X","X","X","X"]]
    print(boxoffour)
    print("printing without for loop")
    for i in boxoffour:
        print(i)
def isfunction():
    x = 5
    y = 6
    print("first trial")
    if x is y:
        print("true")
    else:
        print("false")
    print("second trial")
    y -= 1
    if x is y:
        print("true")
    else:
        print("false")
    print("third trial")    
    t = "5"    
    if x is int(t):
        print("true")
    else:
        print("false")

def splitFunction():
    userInput = input("make your movie, i.e H2 H3")
    move = userInput.split()
    row1 = move[0][0]
    column1 = move[0][1]

    row2 = move[1][0]
    column2 = move[1][1]

def multipleArgumentes(*trial):
    for i in trial:
        print(i)

def splitTest():
    move = 'h2 h3'
    seperated = move.split()
    test = seperated[1][0]
    print(test)
def github():
    print("github is going well")
    print("github is still going well")
    print("attempt to pull from github")
