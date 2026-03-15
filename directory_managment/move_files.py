import os

# Create source and destination folders
os.makedirs("source", exist_ok=True)
os.makedirs("destination", exist_ok=True)

# Create a sample file in source folder
file_path = "source/sample.txt"
with open(file_path, "w") as f:
    f.write("This is a sample file.")

print("\nCreated 'sample.txt' in source folder.")

# Move the file by renaming it to destination path
os.rename(file_path, "destination/sample.txt")
print("File moved to 'destination' folder.")

# Verify contents
print("\nFiles in destination folder:")
print(os.listdir("destination"))