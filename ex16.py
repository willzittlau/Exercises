from sys import argv
script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTR-C (^C).")
print ("If you do want that, hit ENTER.")

input("?")

dot = "."
print ("Opening the file" + dot*5)
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("Writing these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")

target.close()