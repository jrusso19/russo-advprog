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
        board(column1,column2,column3,column4,column5,column6,column7)
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
    print (column1[5], column2[5], column3[5], column4[5], column5[5], column6[5], column7[5])
    print (column1[4], column2[4], column3[4], column4[4], column5[4], column6[4], column7[4])
    print (column1[3], column2[3], column3[3], column4[3], column5[3], column6[3], column7[3])
    print (column1[2], column2[2], column3[2], column4[2], column5[2], column6[2], column7[2])
    print (column1[1], column2[1], column3[1], column4[1], column5[1], column6[1], column7[1])
    print (column1[0], column2[0], column3[0], column4[0], column5[0], column6[0], column7[0])
main()
