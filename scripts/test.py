import json
def count_entries_in_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

        if isinstance(data, list):
            return len(data)
        elif isinstance(data, dict):
            return len(data.keys())
        else:
            return 0


# Example usage
json_file_path = "files/onefile/combined_data.json"  # Replace with the actual path to your JSON file
entry_count = count_entries_in_json_file(json_file_path)
print("Number of entries:", entry_count)