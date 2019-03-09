from matplotlib import pyplot as plt
import matplotlib.animation as animation
import os

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def nohup():
    os.popen("python C:/Users/niall/Documents/College/NetworkManagment/SNMP-Revised/savetograph2.pyw")

nohup()

def animate(i):
    # global i
    # print("test1")
    pullData = open("./Graphstest2.txt", "r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar, yar)
    i = i + 1


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
