import matplotlib.pyplot as plt
import csv
from math import log
def makePlot():

    adict = dict()
    input_size_list = []
    operation_list = list()
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            adict = row
        for key in adict.keys():
            input_size_list.append(key)
        for operation in adict:
            operation_list.append(adict[operation])

    input_size_list = list(map(int, input_size_list))
    operation_list = list(map(int, operation_list))

    nlogn = [x*log(x) for x in input_size_list]

    loggedOperations = [log(x) for x in operation_list]
    loggedInputSize = [log(x) for x in input_size_list]
    plt.gca().set_color_cycle(['red','blue','red'])

    plt.plot(loggedInputSize, loggedOperations)


    plt.legend(['Upper','Actual''Lower'])
    plt.show()

makePlot()
