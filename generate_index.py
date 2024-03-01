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

def get_session_number(folder):
    # Extract the session number from the folder name
    return int(folder.split('sesion')[1])

def generate_index():
    # Define the path to the notes.md file
    notes_path = 'notes.md'  # Assuming notes.md is in the root directory
    
    # Scan the repository for "sesion" folders directly from the root
    sesion_folders = [folder for folder in os.listdir('.') if folder.startswith('sesion') and os.path.isdir(folder)]
    
    print("Session Folders:", sesion_folders)  # Debugging
    
    # Sort session folders based on session number
    sesion_folders.sort(key=lambda x: get_session_number(x))
    
    print("Sorted Session Folders:", sesion_folders)  # Debugging
    
    # Scan Markdown files within the "sesion" folders
    markdown_files = []
    for folder in sesion_folders:
        for file in os.listdir(folder):
            if file.endswith('.md') and file != 'notes.md':
                markdown_files.append(os.path.join(folder, file))
    
    print("Markdown Files:", markdown_files)  # Debugging
    
    # Generate new links for Markdown files
    new_links = []
    for file in markdown_files:
        title = extract_title(file)
        subtitles = extract_subtitles(file)
        filename = f"**{file}:**"
        content_lines = '\n'.join([filename, title] + subtitles)
        new_link = f"{content_lines}\n"
        new_links.append(new_link)
    
    print("New Links:", new_links)  # Debugging
    
    # Write the updated content back to the index page
    with open(notes_path, 'w') as index_file:
        index_file.write('\n'.join(new_links))
    
    print("Index file created successfully.")  # Debugging

if __name__ == "__main__":
    generate_index()


# The generate_index() function scans the repository for Markdown files in folders starting with "sesion" and excludes any files in the root directory.
# The os.path.relpath(root, '.') function is used to get the relative path of the current folder compared to the root directory. If the relative path starts with '.', it means the folder is in the root directory and the file should be excluded.
# Markdown files in the root directory are skipped, ensuring that only files within "sesion" folders are included in the index.
# The get_session_number() function extracts the session number from the folder name.
# The markdown_files list is sorted based on the session number extracted from the folder name.
# Markdown files are sorted numerically according to their session number, ensuring that they appear in the correct order in the index.