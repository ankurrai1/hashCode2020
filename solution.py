import glob

def getFiles():
    return glob.glob("./input/*.in")

def getFileData(fileName):
    f= open(fileName, 'r')
    sliceCount , pizzaType = [int(ip) for ip in next(f).split()]
    for line in f:
        noOfSlices = [int(x) for x in line.split()]
    f.close()
    return(sliceCount,pizzaType,noOfSlices)


files = getFiles()

for fileName in files:
    fileData = getFileData(files[0])
