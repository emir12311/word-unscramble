import random

loopvar = "q"

wordlist = ["clear", "computer", "keyboard", "mouse", "table", "racecar", "legend", "league", "water", "milk", "burger", "spain", "turkey", "france", "britain", "japan", "whiteboard", "eraser", "glass", "bowl", "anime"] 

print("Welcome to the Word Unscrabling game!")
while loopvar != "":
    randnum = random.randint(0, 20)

    pickedword = wordlist[randnum]

    separatedword = list(pickedword)
    random.shuffle(separatedword)

    scrambledword = "".join(separatedword)
    
    
    guess = input(f"The scrambled word is {scrambledword}, can you guess the original word? ")

    if guess.lower() == pickedword.lower():
        print("Congratulations! That was correct")
    else:
        print(f"That guess was wrong, the word was {pickedword}")
    loopvar = input("Press any key + Enter to continue, Press just enter to quit")
        