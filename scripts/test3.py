import json
import os

for file in os.listdir("files/output"):
    if file.endswith(".json"):
        # Read the JSON data from the file
        with open(f"files/output/{file}", 'r') as file:
            data = json.load(file)

            # Iterate through each JSON object in the list
        for item in data:
            # Remove the newline character from archive_file_path field
            item["archive_file_path"] = item["archive_file_path"].strip()

        # Write the modified JSON data back to the file
        with open(f"files/output/{file}", 'w') as file:
            json.dump(data, file, indent=4)