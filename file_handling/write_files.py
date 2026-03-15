f=open("file.txt", "w")
f.write("Hello\n")
f.write("This is sample data\n")
f.write("Python file handling example\n")
f.close()

print("File created and data written.")

f=open("file.txt", "a")
f.write("New line added\n")
f.write("Another appended line\n")
f.close()

print("New lines appended.")
