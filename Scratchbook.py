alist = list()

from math import log
import matplotlib.pyplot as plt

for i in range(1, 10):
    alist.append(i)

newList = list()
print(alist)
alist = [x*2 for x in alist]
print(alist)


input_size_list = [1,2,3,4,5]

logList = [x*log(x) for x in input_size_list]

plt.plot(logList)
plt.show()
print(logList)
