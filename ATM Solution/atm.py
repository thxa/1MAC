def atm(money , request):
# allowed papers: 100, 50, 10, 5, and rest of request
    while request > 0:
        g = "give "
        if money < request:
            print "none"
            break

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
            money -= 2
            request-= 2
            print g + str(2)

        elif request >= 1:
            request -= 1
            print g + str(1)
atm(500, 277)
