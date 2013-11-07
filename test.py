for x in range(1, 101):
    # here goes your solution
    
    if(x % 3 == 0):
        txt = "Fizz"
        if(x % 5 == 0):
            txt = txt + "Buzz"
        print txt
    else:
        if (x % 5 == 0):
            print "Buzz\n"
        else:
        	print x