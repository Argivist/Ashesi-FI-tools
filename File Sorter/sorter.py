import os
import sys

def makeFolder(name):
    if os.path.exists(name):
        return False
    else:
        os.makedirs(name)
        return True
    

def MoveAndRenameFile(file,dest,newName):
    NewPath=os.path.join(dest,newName)
    os.rename(file,NewPath)

def nameStripFormat(name):
    NameParts=name.split('_')
    a_=NameParts[0:2]
    a=a_[0]
    for i in a_[1:]:
        a+='_'+i
    b=NameParts[3:]
    b="_".join(b)
    # b=b[0]
    return a,b
    
def main():
    directoryGiven=False
    # Get target directory from command line argument, default to current directory
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
        directoryGiven=True
    else:
        target_dir = '.'
    
    # Validate the directory exists
    if not os.path.isdir(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist!")
        exit(1)
    
    # Change to the target directory
    # original_dir = os.getcwd()
    # os.chdir(target_dir)
    print(f"Working in directory: {os.path.abspath(target_dir)}\n")
    
    JavaFiles=[]
    for file in os.listdir(target_dir):
        if not file.endswith('.zip') and not file.endswith('.rar') and not file.endswith('.7z') and not file.endswith('.tar') and not file.endswith('.class') and not file.endswith('.py'):
            __name__=nameStripFormat(file)
            f=makeFolder(__name__[0])
            if f:
                print("Created Folder: "+__name__[0])
            else:
                print("Folder already exists: "+__name__[0])
            MoveAndRenameFile(file,__name__[0],__name__[1])
            print("Moved File: "+file+" to Folder: "+__name__[0]+" with new name: "+__name__[1])
    
    # Change back to original directory
    # os.chdir(original_dir)

if __name__ == "__main__":
    main()