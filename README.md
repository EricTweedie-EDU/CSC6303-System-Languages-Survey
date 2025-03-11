# CSC6303-System-Languages-Survey
Repo containing all of the projects for the Systems and Languages Survey

# Contents

# Module 1
Pick a language that you know already (or one that you will learn the basics of now) and convert the Python code in the previous slide into this language.
Python code converted into Java
![image](https://github.com/user-attachments/assets/259a9953-9eab-4c24-8696-7564b182052c)

# Module 2
Convert the C++ program linked below into a Java program.
A program conversion must reproduce the exact behavior, i.e., the same input in the original, and convert programs must deliver the same output. Test ALL data type inputs on both programs.
#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1)                   return false;
    if (n <= 3)                   return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    int number;
    do {
        cout << "Enter a positive number (0 or negative to exit): ";
        cin >> number;
        if (number <= 0)     break;
        if (isPrime(number)) cout << number << " is a prime number." << endl;
        else                 cout << number << " is not a prime number." << endl;
    } while (true);
    return 0;
}

# Module 3
Convert this Python program into a Go lang program. A program conversion must reproduce the exact behavior, i.e., the same input in the original and convert programs must deliver the same output.
![image](https://github.com/user-attachments/assets/d0afa8ed-37bb-4ae0-b37a-2951d1c8e325)

# Module 4
Create an interactive web page using JavaScript. 
Create a web page that receives a number between 2 and 9999 and answers if the number entered is a prime number or not.

# Module 5
Create a Python program that creates a folder and saves a file with 100 random numbers inside this folder.
Your program should ask the user the name of the folder to be created in the current working directory that the program is run in. if the folder exists, the folder has to be removed and a new one created;
Once created, your program should generate 100 random numbers from 0 to 1000 and save them in a file named "numbers100.txt" inside the created folder.
The program must perform system calls to your operating system in order to check if the folder exists, if so, delete it, and then create the folder.

# Module 6
Create a Python program that discovers the current OS and ask the user for a file name and path, and convert it according to the system.
Once your program is aware of the platform, ask the user for a file name with the path (it can be entered according to any format - MacOS or Windows), and your program should convert it to the right format according to the platform and OS the program is running.

# Module 7
Now that you have installed VirtualBox in your machine, install a Linux Ubuntu virtual machine in your VirtualBox, then install VSCode into your Linux, and run last week's coding assignment (week 6) into it.
You have to download an Ubuntu version (feel free to try other OSs if you feel like) then install it in a new VM;
Once installed, open a browser within it (Firefox) and download the appropriated VSCode distribution (.deb);
Just follow the steps in the VSCode page;
Once you have VSCode installed make sure python is working (python3 command is already available at Ubuntu distribution);
Having your VSCode operational for Python, run your Week 6 coding assignment program in there.
You must submit print screens images (photos are ok too) showing that:
You have successfully create a VM for Ubuntu
VSCode is running on your Ubuntu VM
The output of a few runs of your Week 6 assignment program duly running on your Ubuntu VM
Your name somewhere on the screen (perhaps as the user name in your terminal, first last or both is fine)
