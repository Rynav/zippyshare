import re
import os
import json
from urllib.parse import urlparse, unquote

pattern1 = r'\/d\/\w+\/\d+\/\w+\.\w+'
data = []

def extract_filename_from_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    unquoted_path = unquote(path)  # Decode URL-encoded characters

    # Get the filename from the path
    filename = os.path.basename(unquoted_path)

    return filename

def main():
    count = 0
    for file in os.listdir(os.path.join("files")):
        if file.endswith(".cdx"):
            count += 1
            with open(os.path.join("files", file)) as f:
                for line in f:
                    if ".mp3" in line or ".wav" in line:
                        url_pattern = r'https?:\/\/\S+'
                        urls = re.findall(url_pattern, line)

                        data.append({"og_url": urls[0],"file_path": extract_filename_from_url(urls[0]), "file_part": file})
                    print(file)
            with open(os.path.join("files", "output", f"sex{count}.json"), "w") as f1:
                json.dump(data, f1)

            data.clear()

if __name__ == '__main__':
    main()

