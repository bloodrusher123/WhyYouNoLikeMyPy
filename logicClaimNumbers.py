import os
import shutil

videoFileExtensions = ['mp4', 'wmv', 'mov', 'avi', 'mkv', 'flv', 'avchid', 'f4v', 'swf']

def moveVideoFiles(listFilePaths, destinationPath):
    for i in listFilePaths:
        for j in videoFileExtensions:
            if j in i:
                shutil.move(i, destinationPath)
                print('Moved ' + i + ' to ' + j)

def filterClaimNumbers(blobList):
    listClaimNumbers = []
    for i in blobList:
        listClaimNumbers.append(i.split('/')[1])
    filtertedClaimNumberList = filterListClaimNumbers(listClaimNumbers)
    return filtertedClaimNumberList


def filterListClaimNumbers(blobList):
    claimNumberList = list(set(blobList))
    print(claimNumberList)
    return claimNumberList

def createFolder(claimNumber):
    path = 'C://downloads/' + claimNumber
    if not os.path.exists(path):
        os.mkdir(path)
        print('Folder %s created' % path)
    else:
        print('Folder %s already exists' % path)
    
