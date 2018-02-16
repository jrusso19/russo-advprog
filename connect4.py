def main():
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    column6 = []
    column7 = []

    winyet = 0
    p1ok = 1
    p2ok = 1
    while winyet == 0:
        while p1ok == 1:
            player1move = int(input("PLAYER 1 (X): "))
            if player1move in [1,2,3,4,5,6,7,100]:
                print("ok")
                if player1move == 1:
                    column1.append("X")
                elif player1move == 2:
                    column2.append("X")
                elif player1move == 3:
                    column3.append("X")
                elif player1move == 4:
                    column4.append("X")
                elif player1move == 5:
                    column5.append("X")
                elif player1move == 6:
                    column6.append("X")
                elif player1move == 7:
                    column7.append("X")
                elif player1move == 100:
                    p2ok=3
                    winyet=3
                p1ok = 2
            else:
                print("please input a number from 1 to 7.")
        p1ok = 1
        print (winyet)
        print (column3[0])
        board(column1,column2,column3,column4,column5,column6,column7)
        while p2ok == 1:
            player2move = int(input("PLAYER 2 (O): "))
            if player2move in [1,2,3,4,5,6,7,100]:
                print ("ok")
                if player2move == 1:
                    column1.append("O")
                elif player2move == 2:
                    column2.append("O")
                elif player2move == 3:
                    column3.append("O")
                elif player2move == 4:
                    column4.append("O")
                elif player2move == 5:
                    column5.append("O")
                elif player2move == 6:
                    column6.append("O")
                elif player2move == 7:
                    column7.append("O")
                elif player1move == 100:
                    winyet=3
                p2ok = 2
            else:
                print ("please input a number from 1 to 7.")
                p2ok = 1
        p2ok = 1

def board(column1,column2,column3,column4,column5,column6,column7):
    for i in range (7):
        column1.append("-")
        column2.append("-")
        column3.append("-")
        column4.append("-")
        column5.append("-")
        column6.append("-")
        column7.append("-")
    for i in range (6):
        print (column1[6-i], column2[6-i], column3[6-i], column4[6-i], column5[6-i], column6[6-i], column7[6-i])

main()
