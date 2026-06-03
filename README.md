# Smart File Organizer

## Overview

Smart File Organizer is a Python automation tool that automatically organizes files into categorized folders based on their file types. It helps keep directories clean and structured while generating logs and reports of all actions performed.

## Features

* Automatic file organization
* Categorizes files by type
* Duplicate file detection
* Activity logging
* Report generation
* Configurable settings using JSON
* Error handling and logging

## Technologies Used

* Python 3
* os
* shutil
* logging
* json
* hashlib

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project folder:

   ```bash
   cd CodeAlpha_TaskAutomation
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
python organizer.py
```

The program will scan the configured folder, organize files into categories, generate logs, and create reports.

## Project Structure

```text
CodeAlpha_TaskAutomation/
│
├── organizer.py
├── config.json
├── requirements.txt
├── README.md
├── logs/
├── reports/
└── source_files/
```

## Sample Categories

* Images
* Documents
* Videos
* Audio
* Archives
* Code Files

## Author

Created as part of the CodeAlpha Python Programming Internship.
Aruna