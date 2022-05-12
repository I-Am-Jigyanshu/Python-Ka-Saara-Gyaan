counter = {}
def addtoCounter(country):
    if country in counter:
        counter[country] += 1
    else:
        counter[country] = 1

addtoCounter('China')
addtoCounter('India')
addtoCounter('china')
print(len(counter))

