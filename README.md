## Zippyshare indexes and scripts

This repo contains reworked json files containing data for most zippyshare entries, fetched from [here](https://archive.org/details/archiveteam_zippyshare).

### Structures

Every file in ``./files`` has this structure

```json
    {
        "first_part": "file name and subdomain it was downloaded from",
        "archive_date_timestamp": " timestamp of archivization YYYYMMDDHHMMSS",
        "download_link": "link to zippyshare file",
        "response_type": "response type",
        "response_code": "either a response code or '-' ",
        "UNKNOWN1": "don't know what this value means, if you know, make a issue!",
        "UNKNOWN2": "don't know what this value means, if you know, make a issue!",
        "UNKNOWN3": "don't know what this value means, if you know, make a issue!",
        "UNKNOWN4": "don't know what this value means, if you know, make a issue!",
        "UNKNOWN5": "don't know what this value means, if you know, make a issue!",
        "archive_file_path": "path to archive containing this file"
    }
```

### How to download files

If you want to download a single file, you can't.

In order to get this file:
1. Download the 10GB file found in [here](https://archive.org/details/archiveteam_zippyshare), and find file under "archive_file_path".
2. Open it with a warc opener. I recommend [replayweb.page](https://github.com/webrecorder/replayweb.page)
3. Click the link and boom, you get a download!
