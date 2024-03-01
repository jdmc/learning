import os

def extract_titles(filename):
    with open(filename, 'r') as file:
        title = ''
        subtitles = []
        for line in file:
            if line.startswith('# '):
                title = line.strip().lstrip('# ')
            elif line.startswith('## '):
                subtitles.append(line.strip().lstrip('## '))
            elif line.startswith('### '):
                subtitles.append(line.strip().lstrip('### '))
    return title, ', '.join(subtitles)

def generate_index():
    # Define the path to the notes.md file
    notes_path = 'notes.md'  # Assuming notes.md is in the root directory
    
    # Scan the repository for Markdown files recursively
    markdown_files = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.md') and file != 'notes.md':
                markdown_files.append(os.path.relpath(os.path.join(root, file), start='.'))
    
    # Generate new links for Markdown files
    new_links = []
    for file in markdown_files:
        title, subtitles = extract_titles(file)
        new_link = f"- {title}: {subtitles} ({file})"
        new_links.append(new_link)
    
    # Write the updated content back to the index page
    with open(notes_path, 'w') as index_file:
        index_file.write('\n'.join(new_links))

if __name__ == "__main__":
    generate_index()




# os.walk() is used to recursively traverse the directory tree starting from the parent directory (os.pardir) and find all Markdown files.
# os.path.relpath() is used to get the relative path of each Markdown file.
# The script reads all Markdown files found in the learning directory and its subdirectories, excluding notes.md, and updates the index content accordingly.


""" import os

def generate_index():
    # Define the path to the notes.md file
    notes_path = os.path.join(os.pardir, 'notes.md')  # Go up one level to reach the root directory
    
    # Read the existing index page
    with open(notes_path, 'r') as index_file:
        index_content = index_file.read()
    
    # Parse the content to extract existing links
    existing_links = [line.strip() for line in index_content.split('\n') if line.strip().startswith('- ')]
    
    # Scan the repository for Markdown files recursively
    markdown_files = []
    for root, _, files in os.walk(os.pardir):
        for file in files:
            if file.endswith('.md') and file != 'notes.md':
                markdown_files.append(os.path.relpath(os.path.join(root, file), os.pardir))
    
    # Generate new links for Markdown files
    new_links = [f"- [{os.path.splitext(os.path.basename(file))[0]}]({file})" for file in markdown_files]
    
    # Update the existing links with the new links
    updated_content = index_content
    for existing_link, new_link in zip(existing_links, new_links):
        updated_content = updated_content.replace(existing_link, new_link)
    
    # Write the updated content back to the index page
    with open(notes_path, 'w') as index_file:
        index_file.write(updated_content)

if __name__ == "__main__":
    generate_index() """