import random


def rock_paper_scissors():
    p1_count = 0
    p2_count = 0
    game_num = 1

    white = "\33[37m"
    green = "\33[32m"
    red = "\33[31m"
    yellow = "\33[33m"
    blue = "\33[34m"
    sky_blue = "\33[36m"

    print("{} {:^50} {}".format(yellow, "Rock - Paper - Scissors", white))
    print(yellow, "*" * 50, white)

    while True:
        try:
            score = int(input("\33[36m Select Target Score: "))
            print(" Win = 1, Lose/Draw = 0, Target Score =", score, white)
        except ValueError:
            print(red, "\n Invalid Input!")
        else:
            while p1_count < score and p2_count < score:
                print(yellow, "-" * 50)
                print("{:>27} {} {}".format(" Round", game_num, white))

                game = ["Rock", "Paper", "Scissors"]
                p1 = input("\n \33[37mSELECT:\n R for Rock, P for Paper, S for Scissors\n Enter Choice: ")
                p2 = random.choice(game)

                if p1 == "r" or p1 == "R":
                    p1 = game[0]
                elif p1 == "p" or p1 == "P":
                    p1 = game[1]
                elif p1 == "s" or p1 == "S":
                    p1 = game[2]

                print("\n You picked:", p1)
                print(" Computer picked:", p2, white, "\n")

                if p1 == game[0] and p2 == game[1]:
                    print(red, "You Lose, Paper beats Rock", white)
                    p2_count += 1
                elif p1 == game[0] and p2 == game[2]:
                    print(green, "You Win, Rock beats Scissors", white)
                    p1_count += 1
                elif p1 == game[0] and p2 == game[0]:
                    print(blue, "Draw, Rock VS Rock", white)

                elif p1 == game[1] and p2 == game[2]:
                    print(red, "You lose, Scissors beats Paper", white)
                    p2_count += 1
                elif p1 == game[1] and p2 == game[0]:
                    print(green, "You Win, Paper beats Rock", white)
                    p1_count += 1
                elif p1 == game[1] and p2 == game[1]:
                    print(blue, "Draw, Paper VS Paper", white)

                elif p1 == game[2] and p2 == game[0]:
                    print(red, "You lose, Rock beats Scissors", white)
                    p2_count += 1
                elif p1 == game[2] and p2 == game[1]:
                    print(green, "You Win, Scissors beats Paper", white)
                    p1_count += 1
                elif p1 == game[2] and p2 == game[2]:
                    print(blue, "Draw, Scissors VS Scissors", white)
                else:
                    print(red, "Invalid Input!", white)

                game_num += 1
                print('{} {} | Your Score'.format(sky_blue, p1_count))
                print(' {} | Computer Score {:>18} Target Score = {}'
                      .format(p2_count, white, score))

            if p1_count == score:
                print('{} {:_^50} {}'.format(green, "You Win!", white))
                break
            else:
                print('{} {:_^50} {}'.format(red, "You Lose!", white))
                break


rock_paper_scissors()
