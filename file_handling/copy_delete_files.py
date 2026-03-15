import os
import shutil

shutil.copy("file.txt", "file_backup.txt")
print("Backup file created.")


if os.path.exists("file_backup.txt"):
    os.remove("file_backup.txt")
    print("Backup file deleted.")
else:
    print("The file does not exist")

if os.path.exists("myfolder"):
    os.rmdir("myfolder")
    print("Folder removed.")
else:
    f
    print("Folder does not exist")