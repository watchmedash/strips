import os

# Directory containing your HTML files
directory = r'C:\Users\HP\Documents\GitHub\dashflix'  # Replace with your actual directory path

# Line to be removed
line_to_remove = '<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@300;400;500;600;700&display=swap" rel="stylesheet">\n'

def remove_link_tag(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    lines = f.readlines()
                with open(filepath, 'w') as f:
                    for line in lines:
                        if line.strip() != line_to_remove.strip():
                            f.write(line)

# Call the function to remove the specific <link> tag recursively
remove_link_tag(directory)
