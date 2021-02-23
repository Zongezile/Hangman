import random
def play():
    lista = ["python", "java", "kotlin", "javascript"]
    rozwiazanie = random.choice(lista)
    puzzle = list(len(rozwiazanie) * "-")
    puzzle_1 = "".join(puzzle)
    bledy = 0
    litery = ""
    litera = ""
    wszystkie_litery = "abcdefghijklmnopqrstuvwxyz"
    while bledy < 8:
        print("")
        print(puzzle_1)
        litera = input("Input a letter: ")

        if len(litera) != 1:
            print("You should input a single letter")
        elif litera not in wszystkie_litery:
            print("Please enter a lowercase English letter")
        elif litera in litery:
            print("You've already guessed this letter")
        else:
            if litera in rozwiazanie:
                indeksy = []
                for x in range(len(rozwiazanie)):
                    if rozwiazanie[x] == litera:
                        indeksy.append(x)
                for x in indeksy:
                    puzzle[x] = litera
                    puzzle_1 = "".join(puzzle)

                if puzzle_1 == rozwiazanie:
                    print("You guessed the word", rozwiazanie, "!")
                    print("You survived!")
                    break
            elif litera not in rozwiazanie:
                print("That letter doesn't appear in the word")
                bledy += 1
            litery += litera

    if puzzle_1 != rozwiazanie:
         print("You lost!")

print("H A N G M A N")
menu = input("Type 'play' to play the game, 'exit' to quit: ")

while menu != "exit":
    if menu == "play":
        play()
    menu = input("Type 'play' to play the game, 'exit' to quit: ")