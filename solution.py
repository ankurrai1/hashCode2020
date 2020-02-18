import glob

def getFiles():
    return glob.glob("./input/*.in")

def getFileData(fileName):
    file = open(fileName, 'r')
    sliceCount , pizzaType = [int(ip) for ip in next(file).split()]
    for line in file:
        noOfSlices = [int(ip) for ip in line.split()]
    f.close()
    return(sliceCount,pizzaType,noOfSlices)


files = getFiles()

for fileName in files:
    fileData = getFileData(files[0])
