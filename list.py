#!/usr/bin/env python3

import os
import subprocess

def list_directory_contents(directory):
    try:
        ls_output = subprocess.run(['ls', '-l', directory], capture_output=True, text=True, check=True)
        return ls_output.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error listing directory contents: {e}")
        return []

def select_directory(contents):
    while True:
        try:
            choice = int(input("Enter the number of the directory to change into (ignore the '1.' option): "))
            if 1 <= choice <= len(contents):
                chosen_directory = contents[choice - 1].split()[-1]
                return chosen_directory
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def execute_commands_in_directory(directory):
    os.chdir(directory)
    print(f"Changed to directory: {directory}")
    commands = ["ls", "echo Hello World", "pwd"]  # Example commands to execute
    for command in commands:
        subprocess.run(command, shell=True)

def main():
    current_directory = os.getcwd()
    print(f"Contents of directory: {current_directory}")
    contents = list_directory_contents(current_directory)
    for index, item in enumerate(contents, 1):
        print(f"{index}. {item}")
    
    chosen_directory = select_directory(contents)
    execute_commands_in_directory(chosen_directory)

if __name__ == "__main__":
    main()
