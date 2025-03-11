# Eric Tweedie CSC6303 week 6
# Windows 11 OS ver 24H2 build 26100.3194
# Discover the current OS and ask the user for a file name and its path, convert it to the correct format according to the platform and OS
import os
import platform

def os_discover():
    print("Current OS: ", platform.system())
    print("OS name: ", os.name)
    # Ask the user for a file name and its path
    file_name = input("Enter a file name: ")
    file_path = input("Enter the file path: ")
    # Convert file path and name to the correct format according to the platform and OS
    if platform.system() == "Windows":
        file_path = file_path.replace("/", "\\")
        file_name = file_name.replace("\\", " ")
        if not file_path.startswith("C:\\"):
            file_path =  "C:\\" + file_path
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        file_path = file_path.replace("\\", "/")
        file_name = file_name.replace(" ", "\\")
    else:
        print("Unknown OS")
    
    # Combine the file path and name
    file = os.path.join(file_path, file_name)
    print("Converted file path and name: ", file)

os_discover()