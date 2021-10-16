import random, time

white = "\33[37m"
green = "\33[32m"
red = "\33[31m"
yellow = "\33[33m"
blue = "\33[36m"
violet = '\33[35m'


def rules():
    f = open("game-rules.txt", "r")
    print(f.read())


def logo():
    f = open("logo.txt", "r")
    print(f.read())


def win():
    f = open("win.txt", "r")
    return f.read()


def lose():
    f = open("lose.txt", "r")
    return f.read()


def marbles():
    game = ["odd", "even"]
    count_marbles_p1 = 5
    computer = 5
    computer_wager = [1, 2, 3]
    game_round = 1
    inner = 0

    print("\n{} {:^60}".format(yellow, "Marbles - Odd - Even"))
    print("-" * 60, white)

    while count_marbles_p1 > 0 and computer > 0:
        print(yellow, "\n\tRound:", game_round, "\t\tRemaining Marbles", count_marbles_p1, white)
        print("\tTurn:", blue, "player 1", white)
        # wager fix ValueError for invalid input
        wager = int(input("\n\tEnter wager, Between 1 and Remaining Marbles "))

        p1 = input("\n\tGuess: Does the computer have odd or even? ")
        p2 = random.choice(game)

        if p1 == "odd" and p2 == game[0]:
            print("\n\t odd | You picked\n\t", p2, "| Computer had")
            print(blue, "\tPlayer 1 Wins", white)
            count_marbles_p1 += wager
            computer -= wager
            print(green, "\n\t", count_marbles_p1, "| Your Marbles\n\t", computer, "| Computer Marbles", white)
            inner = 0

        elif p1 == "odd" and p2 == game[1]:
            print("\n\t  odd | Your pick\n\t", p2, "| Computer pick")
            print(violet, "\tComputer Wins", white)
            count_marbles_p1 -= wager
            computer += wager
            print(red, "\n\t", count_marbles_p1, "| Your Marbles\n\t", computer, "| Computer Marbles", white)
            inner = 1

        elif p1 == "even" and p2 == game[0]:
            print("\n\teven | Your pick\n\t", p2, "| Computer pick")
            print(violet, "\tComputer Wins", white)
            count_marbles_p1 -= wager
            computer += wager
            print(red, "\n\t", count_marbles_p1, "| Your Marbles\n\t", computer, "| Computer Marbles", white)
            inner = 1

        elif p1 == "even" and p2 == game[1]:
            print("\n\t even | Your pick\n\t", p2, "| Computer pick")
            print(blue, "\tPlayer 1 Wins", white)
            count_marbles_p1 += wager
            computer -= wager
            print(green, "\n\t", count_marbles_p1, "| Your Marbles\n\t", computer, "| Computer Marbles", white)
            inner = 0
        else:
            print(red, "Invalid Input!", white)

        if inner == 1:
            while inner == 1 and count_marbles_p1 > 0 and computer > 0:
                print(yellow, "-" * 60, white)
                game_round += 1
                print(yellow, "\n\tRound:", game_round, "\t\tRemaining Marbles", count_marbles_p1, white)
                print("\tTurn:", violet, "Computer", white)
                print("\n\tComputer Thinking...")
                time.sleep(3)
                p2_wager = random.choice(computer_wager)
                print("\tComputer Wager", p2_wager)
                p1 = input("\n\tPick odd or even and the Computer will try and guess: ")

                p2 = random.choice(game)
                time.sleep(2)

                if p1 == "odd" and p2 == game[0]:
                    print("\n\t", p2, "| Computer pick", "\n\t odd | Your pick")
                    print(violet, "\tComputer Wins", white)
                    computer += p2_wager
                    count_marbles_p1 -= p2_wager
                    print(red, "\n\t", count_marbles_p1, "| Your Marbles\n\t", computer, "| Computer Marbles", white)
                    inner = 1

                elif p1 == "odd" and p2 == game[1]:
                    print("\n\t", p2, "| Computer pick", "\n\t  odd | Your pick")
                    print(blue, "\tPlayer 1 Wins", white)
                    computer -= p2_wager
                    count_marbles_p1 += p2_wager
                    print(green, "\n\t", count_marbles_p1, "| Your Marbles\n\t", computer, "| Computer Marbles", white)
                    inner = 0

                elif p1 == "even" and p2 == game[0]:
                    print("\n\t", p2, " | Computer pick", "\n\t even | Your pick")
                    print(blue, "\tPlayer 1 Wins", white)
                    computer -= p2_wager
                    count_marbles_p1 += p2_wager
                    print(green, "\n\t", count_marbles_p1, "| Your Marbles\n\t", computer, "| Computer Marbles", white)
                    inner = 0

                elif p1 == "even" and p2 == game[1]:
                    print("\n\t", p2, "| Computer pick", "\n\t even | Your pick")
                    print(violet, "\tComputer Wins", white)
                    computer += p2_wager
                    count_marbles_p1 -= p2_wager
                    print(red, "\n\t", count_marbles_p1, "| Your Marbles\n\t", computer, "| Computer Marbles", white)
                    inner = 1
                else:
                    print(red, "Invalid...", white)

        game_round += 1
        print(yellow, "-" * 60, white)

        if count_marbles_p1 >= 10:
            print(green, win())
            print('{} {:_^50} {}'.format(green, "Congratulations", white))
            break
        if computer >= 10:
            print(red, lose())
            print('{} {:_^50} {}'.format(red, "Try Again", white))
            break


def main():
    while True:
        try:
            print(yellow, "*" * 60, green)
            logo()
            print('{} {:^50}'.format(blue, "- - - GAME RULES - - -"))
            rules()
            input("\n\tPress enter to start game ")
        except ValueError:
            print(red, "\n Invalid Input!")
        else:
            marbles()
            print(blue)
            menu = input("\n\tPlay Again? y/n\t")
            if menu == "y":
                continue
            else:
                print("\tGood Bye", white)
                break


if __name__ == "__main__":
    main()
