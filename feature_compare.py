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
            plt.plot(x, y, color = c, label='subject'+person)
            



cont = True
ftype = input("(k/m)?: ")
plt.style.use('seaborn') # pretty matplotlib plots

if ftype == "k":
    action = input("(d/f)?: ")
    key = input("Key(s)?: ")
    plt.title(key + action + " Comparison")
elif ftype == "m":
    action = input("Mouse action?: ")
    feature = int(input("Mouse movement feature?: "))
    plt.title(action + str(feature) + " Comparison")

while cont:    
    ffile = input("filename?: ")
    person = input("Subject?: ")

    if ftype == "k":
        keyCompare(ffile, person, key, action)
    elif ftype == "m":
        mouseCompare(ffile, person, action, feature)
    cont = True if input("Continue? (y/n): ") == "y" else False

handles, labels = plt.gca().get_legend_handles_labels()
newLabels, newHandles = [], []
for handle, label in zip(handles, labels):
  if label not in newLabels:
    newLabels.append(label)
    newHandles.append(handle)
plt.legend(newHandles, newLabels)
plt.show()

    