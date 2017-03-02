import matplotlib.pyplot as plt
import csv

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

    plt.gca().set_color_cycle(['red','blue','red'])
    plt.plot(input_size_list, 1 * operation_list)
    plt.plot(input_size_list, operation_list)
    # plt.plot(input_size_list, 2 * operation_list)
    plt.legend(['Upper','Actual''Lower'])
    plt.show()

makePlot()
# makePlot(1,2)
#
# print(input_size_list)
# print(operation_list)
