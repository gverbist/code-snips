import os

def rename_files_in_directory(to_replace, replace_with):
    # Get the current directory
    current_directory = os.getcwd()
    
    # List all files in the current directory
    files = os.listdir(current_directory)
    
    for filename in files:
        # Check if the filename contains the text to replace
        if to_replace in filename:
            # Create the new filename
            new_filename = filename.replace(to_replace, replace_with)
            # Get the full path for the old and new filenames
            old_file = os.path.join(current_directory, filename)
            new_file = os.path.join(current_directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} -> {new_file}')

if __name__ == "__main__":
    # Take user input
    to_replace = input("Enter the part of the filename to replace: ")
    replace_with = input("Enter the text to replace it with: ")
    
    # Call the function to rename files
    rename_files_in_directory(to_replace, replace_with)

