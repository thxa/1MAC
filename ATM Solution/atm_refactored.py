def withdraw(balance, request):

    if request > balance:
        print("Can't give you all this money !!")

    else:
        r = balance - request

        while request > 0:
            g = "give "

            if request >= 100:
                request -= 100
                print g + str(100)

            elif request >= 50:
                request -= 50
                print g + str(50)

            elif request >= 10:
                request -= 10
                print g + str(10)

            elif request >= 5:
                request -= 5
                print g + str(5)

            elif request >= 2:
                request -= 2
                print g + str(2)

            elif request >= 1:
                request -= 1
                print g + str(1)
    return  r
    print "Current balance = %d"%r


balance = 500
withdraw(balance, 277)
withdraw(balance, 30)
withdraw(balance, 5)
withdraw(balance, 2000)