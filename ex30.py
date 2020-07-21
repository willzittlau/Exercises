people = 30
cars = 40
busses = 15

if cars > people:
    print ("We should take the cars")
elif cars < people:
    print ("We should not take the cars")
else:
    print ("We can't decide.")
    
if busses > cars:
    print ("Thats too much bus")
elif busses < cars:
    print ("Maybe we could take the bus")
else:
    print ("We still can't decide")

if people > busses:
    print ("alright we\'ll take the bus")
else:
    print ("fine let's stay home then")
