# Zip File Extractor

For cases where students submit their files as a zip and you need to extract them all at once.

## Note

Works well with Canvas Format

## To use

1. Place all student zip files in a single folder (one flat directory — no nested subfolders).
   - Ensure each filename follows the Canvas pattern: `studentname_canvasid_assignmentname_filename.zip`  
     Example: `doe_john_12345_assignment1_submission.zip`
   - This is the format _Canvas_ would usually download them in
2. Open the folder the ZipExtractor.py file is in using a terminal/command prompt.
   - you can right click an empty space in the folder it is in and select "Open in Terminal" or "Open Command Window Here"
3. Run the program with the command: `python ZipExtractor.py "path_to_your_folder"`
   - Replace `path_to_your_folder` with the actual path to the folder containing the zip files.
   - Example: `python ZipExtractor.py "C:\Users\YourName\Downloads\StudentFiles"`
   - Each zip file will be extracted to its own folder within the `ExtractedZips` subfolder (e.g., `ExtractedZips/submission_name/`).
   - The original zip files will be moved to a `ZipFiles` subfolder after extraction.
