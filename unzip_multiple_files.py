import os
import zipfile

folder = r"C:\Users\ercix\Downloads\Compressed"  # raw string to avoid \ being interpreted as a special char
extension = ".zip"
new_folder_name = str()
extract_count = int()

# Script Objectives:
# for every zip file in the folder:
# 1. create a folder using zip file name
# 2. extract zip files to created folder
# 3. count zip files extracted

# To do:
# 1. Skip items when folder name already exists

os.chdir(folder)  # change working directory to desired folder

for item in os.listdir(folder):
    if item.endswith(extension):
        # print(item)
        file_name = os.path.abspath(item)       # retrieve the absolute path of the zip file
        zip_ref = zipfile.ZipFile(file_name)    # create zipfile object
        new_folder_name = file_name[36:-4]      # remove folder dir and file extension
        os.mkdir(new_folder_name)               # create a new folder with the zip file name
        zip_ref.extractall(new_folder_name)     # extract files to newly created folder
        zip_ref.close()                         # close file
        # os.remove(file_name)                  # delete zipped file
        print(new_folder_name)
        extract_count += 1

print(f"Extracted {extract_count} zip files")
