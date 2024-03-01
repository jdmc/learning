import os

def extract_contents(filename):
    with open(filename, 'r') as file:
        content = ''
        for line in file:
            content += line
    return content

def extract_title(filename):
    with open(filename, 'r') as file:
        title = ''
        for line in file:
            if line.startswith('# '):
                title = line.strip().lstrip('# ')
                return title
        return ''

def extract_subtitles(filename):
    subtitles = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('## '):
                subtitles.append(line.strip().lstrip('## '))
            elif line.startswith('### '):
                subtitles.append(line.strip().lstrip('### '))
    return subtitles

def generate_index():
    # Define the path to the notes.md file
    notes_path = 'notes.md'  # Assuming notes.md is in the root directory
    
    # Scan the repository for Markdown files in "sesion" folders
    markdown_files = []
    for root, dirs, files in os.walk('.'):
        if any(d.startswith('sesion') for d in dirs):
            for file in files:
                if file.endswith('.md') and file != 'notes.md' and not os.path.relpath(root, '.').startswith('.'):
                    markdown_files.append(os.path.relpath(os.path.join(root, file), start='.'))
    
    # Sort Markdown files alphabetically
    markdown_files.sort()
    
    # Generate new links for Markdown files
    new_links = []
    for file in markdown_files:
        title = extract_title(file)
        subtitles = extract_subtitles(file)
        filename = f"**{file}:**"
        content_lines = '\n'.join([filename, title] + subtitles)
        new_link = f"{content_lines}\n"
        new_links.append(new_link)
    
    # Write the updated content back to the index page
    with open(notes_path, 'w') as index_file:
        index_file.write('\n'.join(new_links))

if __name__ == "__main__":
    generate_index()

# The generate_index() function scans the repository for Markdown files in folders starting with "sesion" and excludes any files in the root directory.
# The os.path.relpath(root, '.') function is used to get the relative path of the current folder compared to the root directory. If the relative path starts with '.', it means the folder is in the root directory and the file should be excluded.
# Markdown files in the root directory are skipped, ensuring that only files within "sesion" folders are included in the index.