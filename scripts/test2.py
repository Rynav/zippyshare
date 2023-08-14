import re
import os
import json

data = []

def extract_information(input_string):
    # Using regular expression to capture the download link
    string = input_string.split(" ")

    # Creating a dictionary to hold the extracted data
    extracted_data = {
        "first_part": string[0],
        "archive_date_timestamp": string[1],
        "download_link": string[2],
        "response_type": string[3],
        "response_code": string[4],
        "UNKNOWN1": string[5],
        "UNKNOWN2": string[6],
        "UNKNOWN3": string[7],
        "UNKNOWN4": string[8],
        "UNKNOWN5": string[9],
        "archive_file_path": string[10].strip()
    }

    return extracted_data

def main():
    count = 0
    for fine in os.listdir("files"):
        count += 1
        data.clear()
        if fine.endswith(".cdx"):
            with open(f"files/{fine}") as f:
                for line in f:
                    if "CDX N b a m s k r M S V g" not in line:
                        print(line)
                        formatted = extract_information(line)
                        print(formatted)
                        data.append(formatted)

            print(fine)
            with open(f"files/output/file{count}.json", "w") as f1:
                json.dump(data, f1, indent=4)


if __name__ == "__main__":
    main()