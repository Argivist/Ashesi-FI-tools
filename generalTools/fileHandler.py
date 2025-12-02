import os 

def makeFolder(name):
    if os.path.exists(name):
        return False
    else:
        os.makedirs(name)
        return True
    

def MoveAndRenameFile(file,dest,newName):
    NewPath=os.path.join(dest,newName)
    os.rename(file,NewPath)

def moveFile(src,dest,name):
    dest=os.path.join(dest,name)
    os.rename(src,dest)