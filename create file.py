import os
import time

# Set the directory path where we want to create files and folders
directory_path = "C:\\Vialume"

try:
    # Check if the directory exists, if not create it
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    while True:
        # Create a new file with a unique name
        filename = f"File_{int(time.time())}.txt"
        file_path = os.path.join(directory_path, filename)
        with open(file_path, "w") as f:
            pass

        print(f"Created new file: {filename}")

        # Create a new folder with a unique name
        folder_name = f"Folder_{int(time.time())}"
        folder_path = os.path.join(directory_path, folder_name)
        os.makedirs(folder_path)

        print(f"Created new folder: {folder_name}")

except Exception as e:
    print(f"An error occurred: {e}")

print("Script execution complete!")
