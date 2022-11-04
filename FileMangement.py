file=open("data.txt","w")
file.write("This is file management demo using python")
file.close()
print("file written successfully")

file=open("data.txt","r")
print(file.read())
file.close()

file=open("data.txt","a")
file.write("\nnow this file is appended.")
file.close()

file=open("data.txt","r")
print(file.read())
file.close()

file=open("data2.txt","w+")
file.write("This is w+ operation using python.")
print("current cursor position: ",file.tell())  
file.seek(0)
print(file.read())
file.close()

