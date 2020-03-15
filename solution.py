import glob
import os.path

def getFiles():
    return glob.glob("./input/*.in")

def getFileData(fileName):
    file = open(fileName, 'r')
    sliceCount , pizzaType = [int(ip) for ip in next(file).split()]
    for line in file:
        noOfSlices = [int(ip) for ip in line.split()]
    file.close()
    return(sliceCount,pizzaType,noOfSlices)

def writeToOutputFile(fileName, result):
    file = open(os.path.join('output', os.path.basename(os.path.splitext(fileName)[0] + '.out')) , 'w')
    file.write(str(len(result))+"\n")
    resultStr = ' '.join([str(slices) for slices in result])
    file.write(resultStr)
    file.close()

def getRequiredPizza(sliceCount,pizzaCount,slices):
    maxNeed = 0
    totalSlices = []
    for i in range(len(slices)-1,-1,-1):
        currentNeed = 0
        currentSlices = []
        for j in range(i,-1,-1):
            currentSlice = slices[j]
            totalNeed = currentNeed + currentSlice
            if totalNeed == sliceCount:
                currentNeed = totalNeed
                currentSlices.append(j)
                break
            elif totalNeed < sliceCount:
                currentNeed = totalNeed
                currentSlices.append(j)
                continue
                
        if maxNeed < currentNeed:
            maxNeed = currentNeed
            totalSlices = currentSlices
    return totalSlices

# Runner code
files = getFiles()
for fileName in files:
    fileData = getFileData(fileName)
    result = getRequiredPizza(fileData[0],fileData[1],fileData[2])
    writeToOutputFile(fileName, result)
