items = [int,float,str,"Jiggu",3,5,6,7,8,43,346,456]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)