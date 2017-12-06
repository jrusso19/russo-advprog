"Make a class BankAccount where instances of accounts can be created. Give these objects variables such as account number, account owner, and account balance. Create methods to deposit, withdraw, and check balance."\

class BankAccount():

    counter = 0

    def __init__(self, name, idnum, balance, change):
        self.name = name
        self.id = idnum
        self.balance = balance
        self.change- change

    def checkbal(self):
        return "Your balance is ", str(self.balance)


listnames = ["Gray", "Coby", "Jake", "Nick"]
listidnum = ["1","2","3","4"]
listbalance = [12662, 86163, 7, 46237819]


go =1
cont =1
while go == 1:
    askname = raw_input("what is your id number?")
    for i in range (0, len(listnames)):
        if askname == listidnum[i]:
            print listnames[i]
    while cont ==1:
        answer = raw_input("Would you like to (c)heck your balance, (w)ithdraw money, (d)eposit money, or (q)uit?")
        if answer == "q":
            cont = 0
        elif answer == "c":
            cont = 1
        elif answer == "w":
            cont = 1
        elif answer == "d":
            cont = 1
        else:
            print "invalid input"
