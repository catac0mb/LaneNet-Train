import os

def rename_files_to_numbers_by_appearance(folder_path, start_number=205):
    try:
        # List all files in the directory
        files = os.listdir(folder_path)

        for index, filename in enumerate(files):
            # Construct the new file name
            new_filename = f"{start_number + index}{os.path.splitext(filename)[1]}"
            # Get full file path
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")

        print("All files have been renamed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_folder_path_here' with the path to your folder
rename_files_to_numbers_by_appearance('C:/image/Additional_images/Right_binary')