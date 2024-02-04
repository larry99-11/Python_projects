#!/usr/bin/env python3

import os
import subprocess
import time

# Delay for 1 second variable
DELAY = 1

bash_script_path = "/Users/emmanuelowusu/python_project/fail_txt.sh"

# Validate the serial number function.
def validate_serial(serial):
    if len(serial) != 7:
        print(f'The SERIAL NUMBER: {serial} is not valid because the maximum number of characters allowed is 7')
        return False
    return True

# List directory contents in long format function.
def list_directory_contents(directory):
    try:
        ls_output = subprocess.run(['ls', '-lt', directory], capture_output=True, text=True, check=True)
        return ls_output.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error listing directory contents: {e}")
        return []  # this will return an empty array

# Prompt the user to choose a directory function
def choose_directory(contents):
    while True:
        try:
            choice = int(input("Enter the number of the directory to change into (ignore the '1.' option): "))
            if 1 <= choice <= len(contents):
                return contents[choice - 1].split()[-1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    try:
        while True:
            print("################## VSWR #################")
            print("#########################################")
            print("                                         ")
            print("## Hit CTRL+C to exit out of the script ##")

            serial_no = input("what is the serial number?: ")
            if not validate_serial(serial_no):
                print("Invalid serial number. Please try again.")
                continue

            Serial_Number_Dir = serial_no
            dir_path = f"/Users/emmanuelowusu/python_project/test_results/systems/{Serial_Number_Dir}/1"

            if not os.path.exists(dir_path):
                print(f'{dir_path} does not exist, please enter a valid serial number.')
                continue

            print("#########################################")
            print("         SERIAL_NUMBER:", serial_no)
            print("#########################################")

            os.chdir(dir_path)
            print("############ Directory Content #################")
            contents = list_directory_contents(dir_path)
            for index, item in enumerate(contents, 1):
                print(f"{index}. {item}")

            chosen_directory = choose_directory(contents)
            print("Changed to directory:", chosen_directory)

            os.chdir(os.path.join(dir_path, chosen_directory, "VSWR/"))

            print("############ VSWR Directory Content #################")
            time.sleep(DELAY)
            ls_output = subprocess.run(['ls', '-lt'], capture_output=True, text=True, check=True)
            print(ls_output.stdout)

            # Converts character to lowercase based on input
            results_ans = input("Would you like to open the results (y/n)? ")
            if results_ans.lower() == 'y':
                subprocess.run(["bash", bash_script_path])
                # Run the .eog command (potentially in the bash script)

            # Converts character to lowercase
            elif results_ans.lower() == 'n':
                print("Ok, continuing VSWR script...")
                exit()

    except KeyboardInterrupt:
        print("\nExiting VSWR script...")

if __name__ == "__main__":
    main()
