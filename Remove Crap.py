import os
import re

#USE THIS FUNCTION ON GIVEN FOLDER, LARGEST DIRECTORY POSSIBLE
def remove_non_tiff_and_non_matching_files(directory):
    allowed_strings = {'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6'}
    #Change the above string for selected tiles.
    for root, dirs, files in os.walk(directory, topdown=False):
        print(f"Checking directory: {root}")
        for file in files:
            print(f"Found file: {file}")
            if not (
                    file.lower().endswith(('.tiff', '.tif')) and  # Change if you need different files
                    'tx' in file.lower() and  # Change the string for different image types
                    any(allowed_string in file for allowed_string in allowed_strings)
            ):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")
            else:
                print(f"Kept (valid file): {file}")

        if not os.listdir(root) and not dirs:
            try:
                os.rmdir(root)
                print(f"Removed empty directory: {root}")
            except Exception as e:
                print(f"Error removing directory {root}: {e}")

# Example usage:
directory_path = 'D:/Research/A2780 Cell Line/A2780 RFP2'
remove_non_tiff_and_non_matching_files(directory_path)

#DO NOT USE THIS
def delete_files_ending_in_odd_number(directory):
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
#directory_path = 'C:/Users/elbak/Desktop/School/Research/Spring 2025 project/A2780Treated'  # Replace with your directory path
#delete_files_ending_in_odd_number(directory_path)