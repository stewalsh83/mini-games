import random, time

# Not finished

white = "\33[37m"
green = "\33[32m"
red = "\33[31m"
yellow = "\33[33m"
blue = "\33[36m"
violet = '\33[35m'

coord = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def board(num):
    print("\n", blue)
    print(' {}{}{}{}{} \t\t1|2|3'.format(num[0][0], "|", num[0][1], "|", num[0][2]))
    print(' {} \t\t-+-+-'.format("-+-+-"))
    print(' {}{}{}{}{} \t\t4|5|6'.format(num[1][0], "|", num[1][1], "|", num[1][2]))
    print(' {} \t\t-+-+-'.format("-+-+-"))
    print(' {}{}{}{}{} \t\t7|8|9'.format(num[2][0], "|", num[2][1], "|", num[2][2]))
    print("\n", white)


def place_xo():
    x = "\33[33mX\33[36m"
    o = "\33[31mO\33[36m"
    count = 0
    count2 = 0
    # if x by default then no need for this
    select = input("Select X: ")

    if select == "x" or select == "X":
        while count < 5:
            user = int(input("Enter number: "))
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
                print("Invalid")
            count += 1

            # if select == "o" or select == "O":
            # count2 = 0
            while count2 < 5:
                print("Computer turn")
                time.sleep(2)
                computer = random.choice(num_lst)
                # user = int(input("Enter number: "))
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
                    print("Invalid")
                count2 += 1
                num_lst.remove(computer)
                break


def main():
    place_xo()


if __name__ == "__main__":
    main()
