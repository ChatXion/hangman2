import random

def hangman():
    wordDict = {'cat': 'household animal', 'dog' : 'household animal',
                'car': 'transportation vehicle', 'apple': 'fruit',
                'zebra' : 'horselike animal', 'monkey':'human cousins',
                'ballon' : 'plastic celebration prop', 'cellphone' : 
                'handheld communicate device', 'spoon' : 'eating utensil',
                'fork' : 'eating utensil','cup' : 'object to pour drinks in',
                'bird' : 'flying animal', 'bat' : 'flying animal'}
    word = genRandWord(wordDict)
    wrong = 0
    stages = ["",
              "________         ",
              "|                ",
              "|       |        ",
              "|       0        ",
              "|      /|\       ",
              "|      / \       ",
              "|                ",
              "|                ",
              ]
    rletters = list(word[0])
    board = ["_"] * len(word[0])
    win = False
    print("Welcome to Hangman")

    gameLoop(wrong,stages,len(stages)-1,rletters,board,win,word)
        
def gameLoop(wrong,stages,lenStages, rletters, board, win,word):
    while wrong < lenStages - 1:
        print("\n")
        print("Hint: {}".format(word[1]))
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word[0]))

def genRandWord(wordDict):
    dictLen = len(wordDict)
    a = random.randint(0,dictLen) - 1
    while a > 0:
        wordDict.popitem()
        a -= 1
    return wordDict.popitem()
