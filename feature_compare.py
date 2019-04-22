import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import csv

def keyCompare(ffile, person, key, action):
    r = open(ffile)
    csv_r = csv.reader(r) 
    if person == '1':
        c = 'r'
    elif person == '2':
        c = 'g'
    elif person == '3':
        c = 'b'
    for row in csv_r:
        if (row[0] == key) & (row[1] == action):
            end = float(row[2])
            start = float(row[3])
            mu = float(row[5])
            sigma = float(row[6])
            x = np.linspace(start,end, 5000)
            y = ss.norm.pdf(x, mu, sigma)
            plt.plot(x, y, color=c, label='subject'+person)
            break

def mouseCompare(ffile, person, action, feature):
    r = open(ffile)
    csv_r = csv.reader(r)
    if person == '1':
        c = 'r'
    elif person == '2':
        c = 'g'
    elif person == '3':
        c = 'b'
    for row in csv_r:
        if row[0] == action:
            end = float(row[5*feature])
            start = float(row[5*feature + 1])
            mu = float(row[5*feature + 3])
            sigma = float(row[5*feature + 4])
            x = np.linspace(start,end, 5000)
            y = ss.norm.pdf(x, mu, sigma)
            plt.plot(x, y, color=c, label='subject'+person)            


dataList = ["_l1", "_l2", "_l3", "_l4", "_l5", "_l6", "_l7", "_l8", "_l9", "_l10", "_b1", "_b2", "_b3", "_b4", "_b5", "_b6", "_b7", "_b8", "_b9", "_b10"]
cont = True
ftype = input("(k/m)?: ")
plt.style.use('seaborn') # pretty matplotlib plots

if ftype == "k":
    action = input("(dwell/flight)?: ")
    key = input("Key(s)?: ")
    plt.title(key + action + " Comparison")
elif ftype == "m":
    action = input("Mouse action?: ")
    feature = int(input("Mouse movement feature? (0-8): "))
    plt.title(action + str(feature) + " Comparison")
iterator = 0
for data in dataList:    
    #ffile = input("filename?: ")
    person = '1' if iterator < 10 else '2'

    if ftype == "k":
        keyCompare("key_features" + data + ".csv", person, key, action)
    elif ftype == "m":
        mouseCompare("mouse_features" + data + ".csv", person, action, feature)
    iterator += 1
    #cont = True if input("Continue? (y/n): ") == "y" else False

handles, labels = plt.gca().get_legend_handles_labels()
newLabels, newHandles = [], []
for handle, label in zip(handles, labels):
  if label not in newLabels:
    newLabels.append(label)
    newHandles.append(handle)
plt.legend(newHandles, newLabels)
plt.show()

    