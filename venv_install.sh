#!/bin/bash

##############################################
#
# Author: EL Owusu
#
# Python virtual machine 
# This script will esentially install the venv for our python projects
#################################################

# Colors
RED="\033[1;31m"
GREEN="\033[1;32m"
ENDCOL="\033[0m"
WHITEITAL="\033[3;1;97m"

#!/bin/bash

# Function to center text
function center() {
    term_width=$(tput cols)
    padding=$(printf '%0.1s' " "{1..500})
    printf '%*.*s %s %*.*s\n' 0 "$(((term_width - 2 - ${#1}) / 2))" "$padding" "$1" 0 "$(((term_width - 1 - ${#1}) / 2))" "$padding"
}

function title_screen() {
    # Clear the screen 
    tput clear

    # Set colors
    tput setaf 3  # Yellow text color
    tput setab 4  # Blue background color

    # Print the colorful border
    printf "\n%*s\n" $(tput cols) | tr ' ' '*'

    # Print the title
    center "VENV: Automation script"

    printf "%*s\n\n" $(tput cols) | tr ' ' '*'

    # Reset colors
    tput sgr0
}


###############################################################################

title_screen

# Prompt for directory name
read -p "Enter the name for your virtual environment directory: " VENV_NAME

# Create virtual environment
python3 -m venv $VENV_NAME

# Check if creation was successful
if [[ $? != 0 ]]; then
    echo -e "${RED}Failed to create the virtual environment.${ENDCOL}"
    exit 1
fi

echo -e "${GREEN}Virtual environment created successfully!${ENDCOL}"

# List contents of the directory
echo -e "${WHITEITAL}##### Contents of $VENV_NAME directory: #####${ENDCOL}"
ls -la $VENV_NAME

echo -e "You can activate the virtual environment using the command: ${WHITEITAL}source $VENV_NAME/bin/activate${ENDCOL}."
