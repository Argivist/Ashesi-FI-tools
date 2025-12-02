import os
import sys
import zipfile

# Add parent directory to Python path to import generalTools
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from generalTools import fileHandler as fh

def extractZip(file,dest):
    """
    file: path to zip file
    dest: destination folder to extract to
    # """
    ExpectedExtractFolder=os.path.splitext(os.path.basename(file))[0]
    dest=os.path.join(dest,ExpectedExtractFolder)
    if not os.path.exists(dest):
        os.makedirs(dest)
    with zipfile.ZipFile(file,'r') as z:
        z.extractall(dest)
        
    # filePotentialFolderName=os.path.splitext(os.path.basename(file))[0]
    # dest=os.path.join(dest,filePotentialFolderName)
    # if not os.path.exists(dest) and not os.listdir(dest):
    #     with zipfile.ZipFile(file,'r') as z:
    #         z.extractall(dest)
    # else:
    #     print("Zip already extracted or folder exists: "+dest)
    #     return 
    
def main():
    if len(sys.argv)<2:
        print("Please provide a zip file to extract.")
        exit(1)
    target_dir = os.path.abspath(sys.argv[1])
    
    if not os.path.isdir(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist!")
        exit(1)
    
    # Create ExtractedZips folder in target directory
    extractZipFolder = os.path.join(target_dir, 'ExtractedZips')
    if not os.path.exists(extractZipFolder):
        os.makedirs(extractZipFolder)
    
    for file in os.listdir(target_dir):
        if file.endswith('.zip'):
            file_path = os.path.join(target_dir, file)
            extractZip(file_path, extractZipFolder)
            print(f"Extracted: {file}")
            
            # Move the zip file to ExtractedZips folder after extraction
            fh.moveFile(file_path, extractZipFolder, file)
            print(f"Moved zip: {file} to {extractZipFolder}")
            
if __name__ == "__main__":
    main()
    main()