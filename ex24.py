print ("Lets practice everything")
print ("You\'d need t know \'bout escapes with \\ that do \n newlines and \t tabs")

poem = ("""
        \t the lovely world
        with logic so firmly planted
        cannot discern \n the needs of love
        nor comprehend passion from intuition
        and requires an explanation
        \n\t where there is none.
        """)

print ("............")
print (poem)
print ("............")

five = 10-2+3-6
print ("this should be five: %s" % five)

def secretformular(started):
    jellybeans = started*500
    jars = jellybeans/1000
    crates=jars/100
    return jellybeans,jars,crates

startpoint = 1000
beans,jars,crates = secretformular(startpoint)

print ("With a starting point of : %d" % startpoint)
print ("We;d have %d beans, %d jars and %d crates" % (beans,jars,crates))

startpoint /= 10
if crates < 1:
    crates = crates + 1

print ("We can also do it this way")
print ("We;d have %d beans, %d jars, and %d crates" % secretformular(startpoint))