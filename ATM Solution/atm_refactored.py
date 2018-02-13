def withdraw(balance, request):

    if request > balance:
        print("Can't give you all this money !!")

    else:
        result = balance - request

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
    return  result
    print "Current balance = %d"%result


balance = 500
withdraw(balance, 277)
withdraw(balance, 30)
withdraw(balance, 5)
withdraw(balance, 2000)