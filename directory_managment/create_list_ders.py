import os

os.mkdir("myfolder")
print("Folder created.")

os.mkdir("testfolder")
print("Second folder created.")

print("Files and folders in current directory:")
print(os.listdir())


import os

#1 Create directory
if not os.path.exists("myfolder"):
    os.mkdir("myfolder")
    print("Folder 'myfolder' created.")

#2 Create nested directories
os.makedirs("myfolder/subfolder1/subfolder2", exist_ok=True)
print("Nested directories created: 'myfolder/subfolder1/subfolder2'")

# 3 List files and folders
print("\nFiles and folders in current directory:")
print(os.listdir())

# 4 Change directory
os.chdir("myfolder")
print("\nCurrent working directory changed to:", os.getcwd())

# 5 List files and folders in 'myfolder'
print("Files and folders in 'myfolder':")
print(os.listdir())

# 6 Go back
os.chdir("..")
print("\nBack to parent directory:", os.getcwd())

# 7 Delete an empty folder
if os.path.exists("myfolder/emptyfolder"):
    os.rmdir("myfolder/emptyfolder")
else:
    os.mkdir("myfolder/emptyfolder")
    print("\nCreated 'emptyfolder' for demonstration")
    os.rmdir("myfolder/emptyfolder")
    print("'emptyfolder' deleted")
    f