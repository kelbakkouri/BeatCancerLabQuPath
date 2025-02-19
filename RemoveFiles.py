import os
import re
import glob

# Define the root directory
directory_path = 'C:/Users/elbak/OneDrive/Desktop/Research/Spring 2025/Images'

# Walk through the directory tree
def delete_non_tiff_files(root_dir):
    # Define a recursive function to delete all files and directories in a directory
    def delete_files_and_directories(directory):
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isdir(file_path):
                delete_files_and_directories(file_path)
            else:
                if not file.endswith('.tif'):
                    os.remove(file_path)
                    print(f'Deleted {file_path}')

        # Remove the directory if it's empty
        if os.path.isdir(directory) and len(os.listdir(directory)) == 0:
            os.rmdir(directory)
            print(f'Deleted directory {directory}')

    # Walk through the directory tree
    for root, dirs, files in os.walk(root_dir):
        # Check if the directory contains any .tif files
        if not any(file.endswith('.tif') for file in files):
            delete_files_and_directories(root)
            continue

        # Check if any non- .tif files exist in the directory
        non_tiff_files = [file for file in files if not file.endswith('.tif')]
        if non_tiff_files:
            # Delete the non- .tif files
            for file in non_tiff_files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f'Deleted {file_path}')


def delete_files_ending_in_even_number(directory):
    """
    Deletes files in the specified directory and all its subdirectories if their names (excluding extensions) end with an odd number.

    :param directory: The path to the directory containing the files.
    """
    # Regex to identify files ending with an odd number before the extension
    odd_number_regex = re.compile(r"\d[02468](\..+)?$")  # Matches numbers 1, 3, 5, 7, 9 before the file extension

    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        print(f"Checking directory: {root}")
        for filename in files:
            if odd_number_regex.search(filename):
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                print(f"Deleted {file_path}")

            # Example usage

  # Replace with your directory path
#delete_non_tiff_files(directory_path)
delete_files_ending_in_even_number(directory_path)