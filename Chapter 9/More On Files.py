f = open("Jiggu")
# print(f.tell()) # Will tell you where is the line you wanna read.
#print(f.readline())
# print(f.tell())
print(f.seek(10)) # resets the line the given position from where it should be read.
print(f.readline())

f.close()

#print(f.readline())