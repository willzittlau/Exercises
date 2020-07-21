i = 0
numbers = []

def while_func(k):
    global i
    while i < k:
        print ("At the top of i is %d:" %i)
        numbers.append(i)

        i += 1
        print ('Numbers now: ', numbers)
        print ("At the bottom i is %d:" %i)

    print ("The numbers:")

    for num in numbers:
        print (num)

while_func(7)