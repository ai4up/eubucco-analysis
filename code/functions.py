
import os
import re

def check_and_read_markdown(file_path, subsection_title):
    # Check if the file exists
    if not os.path.isfile(file_path):
        return f"The file '{file_path}' does not exist."

    # Read the file content
    with open(file_path, 'r') as file:
        content = file.read()

    # Use a regular expression to find the specific subsection
    pattern = re.compile(rf"## {re.escape(subsection_title)}(.*?)(##|$)", re.DOTALL)
    match = pattern.search(content)

    # If the subsection is found, return its content
    if match:
        subsection_content = match.group(1).strip()
        return subsection_content
    else:
        return f"Subsection '{subsection_title}' not found in the file."