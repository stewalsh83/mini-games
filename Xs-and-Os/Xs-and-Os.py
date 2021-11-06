import random, time

# Not finished, See TODO

white = "\33[37m"
green = "\33[32m"
red = "\33[31m"
yellow = "\33[33m"
blue = "\33[36m"
violet = '\33[35m'

coord = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
xgame = []
ogame = []


def logo():
    f = open("logo.txt", "r")
    print(f.read())


def xwin():
    f = open("win.txt", "r")
    print(f.read())


def owin():
    f = open("win2.txt", "r")
    print(f.read())


def draw():
    f = open("draw.txt", "r")
    print(f.read())


def layout():
    f = open("layout.txt", "r")
    print(f.read())


def menu():
    print('{} {:^60}'.format(green, "Main Menu"))
    print("-" * 60, yellow)
    logo()
    print(blue)
    layout()
    print(white)


def board(num):
    print("\n", blue)
    print('\t\t\t {}{}{}{}{} \t\t1|2|3'.format(num[0][0], "|", num[0][1], "|", num[0][2]))
    print('\t\t\t {} \t\t-+-+-'.format("-+-+-"))
    print('\t\t\t {}{}{}{}{} \t\t4|5|6'.format(num[1][0], "|", num[1][1], "|", num[1][2]))
    print('\t\t\t {} \t\t-+-+-'.format("-+-+-"))
    print('\t\t\t {}{}{}{}{} \t\t7|8|9'.format(num[2][0], "|", num[2][1], "|", num[2][2]))
    print("\n", white)


def gameplay():
    if (1 in xgame and 2 in xgame and 3 in xgame) or (4 in xgame and 5 in xgame and 6 in xgame) or (
            7 in xgame and 8 in xgame and 9 in xgame):
        print(yellow)
        xwin()
        print('{} {:^60}'.format(green, "Good Bye"))
        print("-" * 60, white)
        exit()
    elif (1 in xgame and 4 in xgame and 7 in xgame) or (2 in xgame and 5 in xgame and 8 in xgame) or (
            3 in xgame and 6 in xgame and 9 in xgame):
        print(yellow)
        xwin()
        print('{} {:^60}'.format(green, "Good Bye"))
        print("-" * 60, white)
        exit()
    elif (1 in xgame and 5 in xgame and 9 in xgame) or (3 in xgame and 5 in xgame and 7 in xgame):
        print(yellow)
        xwin()
        print('{} {:^60}'.format(green, "Good Bye"))
        print("-" * 60, white)
        exit()

    elif (1 in ogame and 2 in ogame and 3 in ogame) or (4 in ogame and 5 in ogame and 6 in ogame) or (
            7 in ogame and 8 in ogame and 9 in ogame):
        print(red)
        owin()
        print('{} {:^60}'.format(green, "Good Bye"))
        print("-" * 60, white)
        exit()
    elif (1 in ogame and 4 in ogame and 7 in ogame) or (2 in ogame and 5 in ogame and 8 in ogame) or (
            3 in ogame and 6 in ogame and 9 in ogame):
        print(red)
        owin()
        print('{} {:^60}'.format(green, "Good Bye"))
        print("-" * 60, white)
        exit()
    elif (1 in ogame and 5 in ogame and 9 in ogame) or (3 in ogame and 5 in ogame and 7 in ogame):
        print(red)
        owin()
        print('{} {:^60}'.format(green, "Good Bye"))
        print("-" * 60, white)
        exit()

    elif sum(num_lst) == 0:
        print(blue)
        draw()
        print('{} {:^60}'.format(green, "Good Bye"))
        print("-" * 60, white)
        exit()


def place_xo():
    x = "\33[33mX\33[36m"
    o = "\33[31mO\33[36m"
    count = 0
    count2 = 0

    while True:
        try:
            select = input("\t\t\t Select X or O: ")
            print("\n")
        except ValueError:
            print("")
        else:
            if select == "x" or select == "X":
                while count < 5:
                    print(blue, "- " * 30, white)
                    user = int(input("\t\t\t Enter number: "))
                    # appends input into new list to track gameplay
                    xgame.append(user)
                    # removes input from list to limit selections
                    num_lst.remove(user)

                    if user == 1:
                        coord[0].pop(0)
                        coord[0].insert(0, x)
                        board(coord)
                    elif user == 2:
                        coord[0].pop(1)
                        coord[0].insert(1, x)
                        board(coord)
                    elif user == 3:
                        coord[0].pop(2)
                        coord[0].insert(2, x)
                        board(coord)
                    elif user == 4:
                        coord[1].pop(0)
                        coord[1].insert(0, x)
                        board(coord)
                    elif user == 5:
                        coord[1].pop(1)
                        coord[1].insert(1, x)
                        board(coord)
                    elif user == 6:
                        coord[1].pop(2)
                        coord[1].insert(2, x)
                        board(coord)
                    elif user == 7:
                        coord[2].pop(0)
                        coord[2].insert(0, x)
                        board(coord)
                    elif user == 8:
                        coord[2].pop(1)
                        coord[2].insert(1, x)
                        board(coord)
                    elif user == 9:
                        coord[2].pop(2)
                        coord[2].insert(2, x)
                        board(coord)
                    else:
                        print(red, "Invalid", white)
                    count += 1
                    gameplay()

                    while count2 < 5:
                        print("\t\t\t Computers turn...")
                        time.sleep(2)
                        computer = random.choice(num_lst)
                        ogame.append(computer)

                        if computer == 1:
                            coord[0].pop(0)
                            coord[0].insert(0, o)
                            board(coord)
                        elif computer == 2:
                            coord[0].pop(1)
                            coord[0].insert(1, o)
                            board(coord)
                        elif computer == 3:
                            coord[0].pop(2)
                            coord[0].insert(2, o)
                            board(coord)
                        elif computer == 4:
                            coord[1].pop(0)
                            coord[1].insert(0, o)
                            board(coord)
                        elif computer == 5:
                            coord[1].pop(1)
                            coord[1].insert(1, o)
                            board(coord)
                        elif computer == 6:
                            coord[1].pop(2)
                            coord[1].insert(2, o)
                            board(coord)
                        elif computer == 7:
                            coord[2].pop(0)
                            coord[2].insert(0, o)
                            board(coord)
                        elif computer == 8:
                            coord[2].pop(1)
                            coord[2].insert(1, o)
                            board(coord)
                        elif computer == 9:
                            coord[2].pop(2)
                            coord[2].insert(2, o)
                            board(coord)
                        else:
                            print(red, "Invalid", white)
                        count2 += 1
                        # removes input from list to limit selections
                        num_lst.remove(computer)
                        gameplay()
                        break

            if select == "o" or select == "O":
                while count2 < 5:
                    print(blue, "- " * 30, white)
                    print("\t\t\t Computers turn...")
                    time.sleep(2)
                    computer = random.choice(num_lst)
                    xgame.append(computer)

                    if computer == 1:
                        coord[0].pop(0)
                        coord[0].insert(0, x)
                        board(coord)
                    elif computer == 2:
                        coord[0].pop(1)
                        coord[0].insert(1, x)
                        board(coord)
                    elif computer == 3:
                        coord[0].pop(2)
                        coord[0].insert(2, x)
                        board(coord)
                    elif computer == 4:
                        coord[1].pop(0)
                        coord[1].insert(0, x)
                        board(coord)
                    elif computer == 5:
                        coord[1].pop(1)
                        coord[1].insert(1, x)
                        board(coord)
                    elif computer == 6:
                        coord[1].pop(2)
                        coord[1].insert(2, x)
                        board(coord)
                    elif computer == 7:
                        coord[2].pop(0)
                        coord[2].insert(0, x)
                        board(coord)
                    elif computer == 8:
                        coord[2].pop(1)
                        coord[2].insert(1, x)
                        board(coord)
                    elif computer == 9:
                        coord[2].pop(2)
                        coord[2].insert(2, x)
                        board(coord)
                    else:
                        print(red, "Invalid", white)
                    count2 += 1
                    # removes input from list to limit selections
                    num_lst.remove(computer)
                    gameplay()

                    while count < 5:
                        user = int(input("\t\t\t Enter number: "))
                        ogame.append(user)
                        # removes input from list to limit selections
                        num_lst.remove(user)

                        if user == 1:
                            coord[0].pop(0)
                            coord[0].insert(0, o)
                            board(coord)
                        elif user == 2:
                            coord[0].pop(1)
                            coord[0].insert(1, o)
                            board(coord)
                        elif user == 3:
                            coord[0].pop(2)
                            coord[0].insert(2, o)
                            board(coord)
                        elif user == 4:
                            coord[1].pop(0)
                            coord[1].insert(0, o)
                            board(coord)
                        elif user == 5:
                            coord[1].pop(1)
                            coord[1].insert(1, o)
                            board(coord)
                        elif user == 6:
                            coord[1].pop(2)
                            coord[1].insert(2, o)
                            board(coord)
                        elif user == 7:
                            coord[2].pop(0)
                            coord[2].insert(0, o)
                            board(coord)
                        elif user == 8:
                            coord[2].pop(1)
                            coord[2].insert(1, o)
                            board(coord)
                        elif user == 9:
                            coord[2].pop(2)
                            coord[2].insert(2, o)
                            board(coord)
                        else:
                            print(red, "Invalid", white)
                        count += 1
                        gameplay()
                        break
            else:
                print(red, "\nInvalid Input!\n", white)


def main():
    while True:
        menu()
        play = input("\t\t\t Play? y/n ")
        print("\n")
        if play == "y" or play == "Y":
            place_xo()
        else:
            print('{} {:^60}'.format(green, "Good Bye"))
            print("-" * 60, white)
            exit()


if __name__ == "__main__":
    main()
