import os

# Directory containing your HTML files
directory = r'C:\Users\HP\Documents\GitHub\dashflix'  # Replace with your actual directory path

# Line to be removed (without newline character)
line_to_remove = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2412399424552673" crossorigin="anonymous"></script>'

def remove_line_from_files(directory, line_to_remove):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                temp_filepath = filepath + '.tmp'
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    with open(temp_filepath, 'w', encoding='utf-8') as f:
                        for line in lines:
                            # Strip newline characters for comparison
                            if line.strip() != line_to_remove:
                                f.write(line)

                    # Replace the original file with the updated file
                    os.replace(temp_filepath, filepath)

                except PermissionError:
                    print(f"Permission error with file {filepath}. Ensure the file is not open and you have necessary permissions.")
                except Exception as e:
                    print(f"Error processing file {filepath}: {e}")

# Call the function to remove the specific line recursively
remove_line_from_files(directory, line_to_remove)
