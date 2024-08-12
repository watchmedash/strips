import os

def split_html_file(input_file, lines_per_file, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    num_files = (total_lines // lines_per_file) + (1 if total_lines % lines_per_file != 0 else 0)

    for i in range(num_files):
        start_line = i * lines_per_file
        end_line = start_line + lines_per_file
        part_lines = lines[start_line:end_line]

        part_filename = os.path.join(output_dir, f'gallery-part{i + 1}.html')
        with open(part_filename, 'w', encoding='utf-8') as part_file:
            part_file.writelines(part_lines)
        
        print(f'Split part {i + 1} saved to {part_filename}')

if __name__ == '__main__':
    # Customize the following variables
    input_file = 'large-gallery.html'  # Your large HTML file
    lines_per_file = 10008  # Number of lines per split file
    output_dir = 'split-gallery'  # Directory to save split files

    split_html_file(input_file, lines_per_file, output_dir)
