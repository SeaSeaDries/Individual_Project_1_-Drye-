import os
name = "Cc"

file_name = input("Enter a messenger file name that ends in .txt: ")

if os.path.exists(file_name):
    file = open(file_name, "r")
    print(file.read()) 
    file.close()
else:
    print(f"\n{file_name} does not exist. A new file will be created instead")

new_message = input("Enter a message: ")

file = open(file_name, "a")
file.write(f"[{name}]: {new_message}\n")
file.close()

print("New message has been saved")