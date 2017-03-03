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


    loggedOperations = [log(x) for x in operation_list]
    loggedInputSize = [log(x) for x in input_size_list]

    Lnlogn = [x*log(x)*2 for x in loggedInputSize]
    Unlogn = [x*log(x)*-2 for x in loggedInputSize]

    plt.gca().set_color_cycle(['red','blue','red'])
    plt.plot(Lnlogn)
    plt.plot(loggedOperations)


    plt.legend(['Upper-Scalar','Actual''Lower-Scalar'])
    plt.show()

makePlot()
