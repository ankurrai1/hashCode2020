import glob

def getFiles():
    return glob.glob("./input/*.in")

files = getFiles()

for fileName in files:
    print(fileName)
