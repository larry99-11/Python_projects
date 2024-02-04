#!/usr/bin/env python3
import os
import subprocess
import time

t = 1

print("################## VSWR #################")
print("#########################################")


serial_no = input("what is the serial number?: ") 
print("#########################################")

Serial_Number_Dir = serial_no

dir_path = "test_results/systems/{}/1".format(Serial_Number_Dir)


# if numbers are longer/less than 7 chraters return an error
if len(serial_no) != 7:
    print(f'The SERIAL NUMBER: {serial_no} is not valid because the maximum number of characters allowed is 7')
    serial_no = input('please re-enter the serial number: ')

if not os.path.exists(dir_path):
    print(f'{dir_path} do not exit, exiting script')
    exit()
    
print("#########################################")
print("         SERIAL_NUMBER:", serial_no)
print("#########################################")

os.chdir(dir_path)

#once in the directory i want to have a long list the contents i.e files
print("############ Directory Content #################")

#takes the output of the ls command
ls_output = subprocess.run(['ls', '-lt'], capture_output=True, text=True)

    #if the ls command was sucessful
if ls_output.returncode == 0:
    # Split the output into lines and store in an array
    directory_contents = ls_output.stdout.splitlines()
    # Display the array contents with indices i.e numbered options to select from
    for index, item in enumerate(directory_contents, 1):
        print(f"{index}. {item}")
    # Prompt the user to choose a directory
    while True:
        try:
            choice = int(input("Enter the number of the directory to change into: "))
            if 1 <= choice <= len(directory_contents):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    # Extract the directory name from the chosen line
    chosen_directory = directory_contents[choice - 1].split()[-1]
    # Change to the chosen directory
    try:
        os.chdir(chosen_directory)
        print("Changed to directory:", chosen_directory)
        #go into VSWR directory
        print("##### changing to VSWR directory #########")
        os.chdir("VSWR/")
        print("###### listing contents #######")

        time.sleep(t)
        subprocess.run(['ls', '-lt'])

        results_ans = input("would you like to open the results (y/n)? ")
        #will have to tweak this as we have to look for 'FAIL' keyword with grep
        if results_ans == 'y':

                command_1 = "cat log.txt | grep -i 'FAIL'; eog *.png"
                subprocess.run(command_1, shell = True) #this will execute shell commands

        elif results_ans == 'n':
            print("Ok exiting VSWR script...")
            exit()

    #error checkng if VSWR dir don't exist  
    except FileNotFoundError:
        print("Directory not found:", chosen_directory)
else:
    print("Error executing ls -lt command:", ls_output.stderr)

