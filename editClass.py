import os, re
#flat = 2
PATH = 'dataset/Mister Potato Sour Cream'
PATH1 = 'dataset'

for file in os.listdir(PATH):
    Name, fType = os.path.splitext(file)
    if fType == ".txt":
        openedFile = open(PATH + '/' + file, 'r')
        linesArray = []
        for line in openedFile:
            values = re.split('\s+', line.rstrip())
            newLine = "6" + " " + values[1] + " " + values[2] + " " + values[3] + " " + values[4]
            linesArray.append(newLine)
            # print(values[0])

        print(linesArray)
        print(file)
        outfile = open(PATH + '/' + file, 'w')
        for line2 in linesArray:
            outfile.write(line2 + '\n')
