#Create a Dictionary and take input from user and return the meaning of the word from the dictionary.
print("So which word meaning do you want: ")
n=input()
D = {"Mutable":"Can Change",
     "Immutable":"Cannot Change",
     "Python":"Coding",
     "Programming":"Love"}
print("The word ",n,"meaning is :",D[n])
