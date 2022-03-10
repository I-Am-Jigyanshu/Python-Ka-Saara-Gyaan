"""
# f = open("Jiggu", "w") writing ke liye
f= open("Jiggu","a") # Append ke liye
a = f.write("Jiggu bhai khatarnak..\n")
print(a)
f.close()
"""
# Handle read and write both.
f= open("Jiggu", "r+")
print(f.read())
f.write("thankyou")