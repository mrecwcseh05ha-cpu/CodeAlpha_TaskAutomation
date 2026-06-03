import os
import json
import shutil
import hashlib
import logging

from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"

)

with open("config.json", "r") as file:
    config = json.load(file)

CATEGORIES = config["categories"]

SOURCE_FOLDER = "source_files"

def get_file_hash(filepath):
    hasher = hashlib.md5()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()
def organize_files():
    duplicates = {}

    for filename in os.listdir(SOURCE_FOLDER):

        filepath = os.path.join(SOURCE_FOLDER, filename)

        if not os.path.isfile(filepath):
            continue

        file_hash = get_file_hash(filepath)

        if file_hash in duplicates:

            duplicate_folder = os.path.join(
                SOURCE_FOLDER,
                "Duplicates"
            )

            os.makedirs(
                duplicate_folder,
                exist_ok=True
            )

            shutil.move(
                filepath,
                os.path.join(
                    duplicate_folder,
                    filename
                )
            )

            print(
                f"{Fore.RED}Duplicate: {filename}"
            )

            continue

        duplicates[file_hash] = filename

        extension = os.path.splitext(
            filename
        )[1].lower()

        category = CATEGORIES.get(
            extension,
            "Others"
        )

        destination = os.path.join(
            SOURCE_FOLDER,
            category
        )

        os.makedirs(
            destination,
            exist_ok=True
        )

        shutil.move(
            filepath,
            os.path.join(
                destination,
                filename
            )
        )

        logging.info(
            f"Moved {filename} -> {category}"
        )

        print(
            f"{Fore.GREEN}Moved {filename} -> {category}"
        )

def generate_report():

    os.makedirs(
        "reports",
        exist_ok=True
    )

    report_path = (
        f"reports/report_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(
        report_path,
        "w"
    ) as report:

        report.write(
            "SMART FILE ORGANIZER REPORT\n\n"
        )

        report.write(
            f"Generated: {datetime.now()}\n\n"
        )

        for folder in os.listdir(
            SOURCE_FOLDER
        ):

            folder_path = os.path.join(
                SOURCE_FOLDER,
                folder
            )

            if os.path.isdir(folder_path):

                count = len(
                    os.listdir(folder_path)
                )

                report.write(
                    f"{folder}: {count} files\n"
                )

    print(
        f"{Fore.CYAN}Report Generated"
    )
if __name__ == "__main__":

    organize_files()

    generate_report()

    print(
        f"{Fore.YELLOW}Organization Completed!"
    )