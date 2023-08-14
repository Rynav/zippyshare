import os
import json

def is_json_file_empty(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return not bool(data)  # Check if the loaded data is empty

def remove_empty_json_files(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith(".json"):
            file_path = os.path.join(directory, file_name)
            if is_json_file_empty(file_path):
                os.remove(file_path)
                print(f"Removed empty file: {file_path}")

# Example usage
directory_path = "files/output/"  # Replace with the actual directory path
remove_empty_json_files(directory_path)
