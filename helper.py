from random import randrange
import csv
def makeHuffmanInput(n):
    f = []
    for ii in range(1,n):
        f.append(randrange(1,100))
    return f


def writeCSV(adict_data):
    with open('data.csv', 'w', newline = '') as f:
        writer = csv.DictWriter(f, adict_data)
        writer.writeheader()
        writer.writerow(adict_data)


#Will write this to data
# writeCSV({"Error": 404})
