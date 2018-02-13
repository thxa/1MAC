class ATM:
    def __init__(self ,balance , bank_name ):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):

        print "welcome to " + self.bank_name
        print "Current balance = %d" %self.balance
        print "=" * 34

        if request > self.balance:
            print("Can't give you all this money !!")

        else:
            self.balance  -= request
            while request > 0:
                give_string = "give "

                if request >= 100:
                    request -= 100
                    print give_string + str(100)

                elif request >= 50:
                    request -= 50
                    print give_string + str(50)

                elif request >= 10:
                    request -= 10
                    print give_string + str(10)

                elif request >= 5:
                    request -= 5
                    print give_string + str(5)

                elif request >= 2:
                    request -= 2
                    print give_string + str(2)

                elif request >= 1:
                    request -= 1
                    print give_string + str(1)
        print "=" * 34
        return  self.balance


if __name__ == '__main__':
    balance1 = 500
    balance2 = 1000

    atm1 = ATM(balance1, "Smart Bank")
    atm2 = ATM(balance2, "Baraka Bank")

    atm1.withdraw(277)
    atm1.withdraw(800)

    atm2.withdraw(100)
    atm2.withdraw(2000)