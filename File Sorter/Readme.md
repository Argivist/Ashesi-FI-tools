# Student file sorter

For cases where students submit their files outside a zip file that is individually.

## Note

Works well with Canvas Format

## To use

1. Place all student files in a single folder (one flat directory — no nested subfolders).
   - Ensure each filename follows the Canvas pattern: `studentname_canvasid_assignmentname_filename.extension`  
     Example: `doe_john_12345_assignment1_report.pdf`
   - This is the format _Canvas_ would usually download them in
2. Open the folder the sorter.py file is in using a terminal/command prompt.
   - you can right click an empty space in the folder it is in and select "Open in Terminal" or "Open Command Window Here"
3. Run the program with the command: `python sorter.py "path_to_your_folder"`
   - Replace `path_to_your_folder` with the actual path to the folder containing the student files.
   - Example: `python sorter.py "C:\Users\YourName\Downloads\StudentFiles"`
   - You can simply run `python sorter.py` to sort files in the current directory.
