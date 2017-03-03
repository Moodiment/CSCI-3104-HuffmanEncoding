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

    Unlogn = [2*x*log(x,2) for x in input_size_list]
    Lnlogn = [.5*x*log(x,2) for x in input_size_list]
    plt.gca().set_color_cycle(['red','blue','red'])
    # plt.plot(Lnlogn)
    plt.plot(input_size_list,Unlogn)
    plt.plot(input_size_list,operation_list)
    plt.plot(input_size_list,Lnlogn)


    plt.legend(['Upper-Scalar','Actual','Lower-Scalar'])
    plt.title("Huffman Encode experiment")
    # plt.axis("")
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel("number of operations, T")
    plt.xlabel("Input size, n")
    plt.show()

makePlot()
