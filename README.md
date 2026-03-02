# Introduction

Identifile is a file-type identification web application that uses a file's "magic number" to identify its real format, regardless of the file extension or name.
It is a tool meant for those who want to validate any files with unknown file types, and can also be used for forensics or inspection as the tool scans for embedded signatures.

# Features

* Uses a file signature database to detect the file type. The database includes common file formats like PNG, JPG and MP4.
* Scans for embedded files, which are files within the main file.
* Coded such that it only scans the first 256KB of the uploaded file.
* Supports drag-and-drop.
* Has XSS-protection.

# State of the Project

<p>This tool has its limitations, as mentioned it only scans the first 256KB of the file.</p>
<p>It has not been deployed yet.</p>
<p>It is still being updated.</p>
<p>The public is free to use, copy, modify and publish any part of the code. I encourage you to scale up the tool to be more robust.</p>

# Stack

### Backend

* Python
* FastAPI

### Frontend

* HTML
* CSS
* JS Fetch API

# Running It Locally

1. Clone the repository:

   ```
   git clone https://github.com/kangindustries/Identifile.git
   ```

2. Create the virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```
   venv\Scripts\activate
   ```

4. If you encounter issues with PowerShell permissions:

   ```
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

5. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Startup the server:

   ```
   uvicorn app:app --reload
   ```


