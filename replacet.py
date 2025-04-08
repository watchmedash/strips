import os
import fileinput

def replace_text_in_files(directory, old_text, new_text):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".html"):  # Only include .html files
                filepath = os.path.join(root, filename)
                with fileinput.FileInput(filepath, inplace=True, encoding='utf-8') as file:
                    for line in file:
                        print(line.replace(old_text, new_text), end='')

# Replace the script in all HTML files in the current directory and its subdirectories
replace_text_in_files('.', 'dashflix.xyz', 'dashflix.top')
