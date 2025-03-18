#!/bin/bash

# write a bash script to get the directory path from the user,
# check if it exists, and create the file if not.


# get directory name from user
echo "Enter the name of the directory to check for..."
read USER_INPUT

# check if directory exist
if [ -d "$USER_INPUT" ]; then
    echo "The directory '$USER_INPUT' already exist."
else
    # create directory
    echo "Directory does not exist, trying to create directory '$USER_INPUT'..."
    mkdir -p "$USER_INPUT"
    # check if directory creation was successful
    if [ $? -eq 0 ]; then
        echo "The directory '$USER_INPUT' has been successfully created."
    else
        echo "Failed to create directory, '$USER_INPUT'"
    fi 
fi