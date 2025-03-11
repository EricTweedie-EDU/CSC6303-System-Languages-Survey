# Eric Tweedie week 5 C#C 6303
# OS: Windows 11 ver: 24H2 build 26100.3194
# Python program that creates a folder and file in users current directory

import os
import random

# Create a folder, if folder already exists, delete and recreate
def create_folder(folder):
    try:
        if folder not in os.listdir():
            os.mkdir(folder)
        else:
            if os.path.exists(folder):
                print("Folder already exists, folder will be deleted and recreated")
                if os.listdir(folder) != []:
                    for file in os.listdir(folder):
                        os.remove(folder + '/' + file)
                os.rmdir(folder)
                os.mkdir(folder)
            
    except Exception as e:
        print(e)

# Create a file in the folder with 100 random numbers from 0 to 1000
def create_file(folder):
    try:
        with open(folder + '/numbers100.txt', 'w') as file:
            for _ in range(100):
                file.write(str(random.randint(0, 1000)))
                file.write('\n')

    except Exception as e:
        print(e)


# Main function
def main():
    print("Creating folder and file in current directory")
    folder = input("Enter folder name:")
    create_folder(folder)
    create_file(folder)
    print("Folder and file created successfully")


if __name__ == "__main__":
    main()