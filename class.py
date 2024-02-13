import subprocess
import os

class File:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def check_permissions(self):
        # Check permissions of the file
        return os.access(self.file_name, os.X_OK)  # Check for execution access
    
    def change_permissions(self, mode):
        # Change permissions of the file
        try:
            subprocess.run(['chmod', mode, self.file_name], check=True)
            
        except subprocess.CalledProcessError:
            print(f"Error: Failed to change permissions of {self.file_name}")

    def execute_script(self):
        # Run the script 
        try:
            subprocess.run(["bash", self.file_name], check=True)
        except subprocess.CalledProcessError:
            print(f"Error: Failed to execute {self.file_name}")

# File to work with
file_name = "IQ_Gain.sh"
my_file = File(file_name)

# Check current permissions
if not my_file.check_permissions():
    print(f"{file_name} does not have execute permissions! Changing permissions now...")
    my_file.change_permissions("u+x")

# Check current permissions again
current_permissions = "executable" if my_file.check_permissions() else "not executable"
print(f"Current permissions of {file_name}: {current_permissions}")

# Execute the script
print(f"Executing {file_name}...")
my_file.execute_script()
