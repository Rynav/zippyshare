import os
import json

input_folder = "files/output/"  # Change this to the directory containing your JSON files
output_file = "files/onefile/combined_data.json"  # Change this to the desired name of the output JSON file

combined_data = []




# Iterate over each file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".json"):
        file_path = os.path.join(input_folder, file_name)
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                combined_data.extend(data)
            except json.JSONDecodeError:
                print(f"Error reading JSON from {file_name}")

# Write the combined data to the output JSON file
with open(output_file, "w") as output:
    json.dump(combined_data, output, indent=4)

print("Combined data written to", output_file)