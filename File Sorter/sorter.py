import os
import sys

# Add parent directory to Python path to import generalTools
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from generalTools import fileHandler as fh

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
    
    # Convert to absolute path to avoid path issues
    target_dir = os.path.abspath(target_dir)
    print(f"Working in directory: {target_dir}\n")
    
    JavaFiles=[]
    for file in os.listdir(target_dir):
        if not file.endswith('.zip') and not file.endswith('.rar') and not file.endswith('.7z') and not file.endswith('.tar') and not file.endswith('.class') and not file.endswith('.py'):
            __name__=nameStripFormat(file)
            
            # Create folder in target directory
            folder_path = os.path.join(target_dir, __name__[0])
            f=fh.makeFolder(folder_path)
            if f:
                print("Created Folder: "+__name__[0])
            else:
                print("Folder already exists: "+__name__[0])
            
            # Move file with full path
            file_path = os.path.join(target_dir, file)
            fh.MoveAndRenameFile(file_path, folder_path, __name__[1])
            print("Moved File: "+file+" to Folder: "+__name__[0]+" with new name: "+__name__[1])
    
    # Change back to original directory
    # os.chdir(original_dir)

if __name__ == "__main__":
    main()