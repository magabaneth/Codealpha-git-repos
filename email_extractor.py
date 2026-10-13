"""
CodeAlpha Task 3: Task Automation with Python Scripts
Automation idea: extract all email addresses from a .txt file
and save them to another file.

Usage:
    python email_extractor.py                      # uses default file names
    python email_extractor.py input.txt output.txt # custom file names
"""

import os
import re
import sys

DEFAULT_INPUT = "sample_input.txt"
DEFAULT_OUTPUT = "extracted_emails.txt"


EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def read_file(path):
    """Read and return the full text of a file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_emails(text):
    """Find all email addresses in the text, remove duplicates, keep order."""
    found = re.findall(EMAIL_PATTERN, text)
    unique = []
    seen = set()
    for email in found:
        key = email.lower()
        if key not in seen:
            seen.add(key)
            unique.append(email)
    return unique


def save_emails(emails, path):
    """Write one email address per line to the output file."""
    with open(path, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    output_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUTPUT

    if not os.path.exists(input_path):
        print(f"Error: input file '{input_path}' was not found.")
        return

    text = read_file(input_path)
    emails = extract_emails(text)

    if not emails:
        print("No email addresses found.")
        return

    save_emails(emails, output_path)
    print(f"Found {len(emails)} unique email address(es):")
    for email in emails:
        print(f"  {email}")
    print(f"\nSaved to '{output_path}'.")


if __name__ == "__main__":
    main()
