import os

def generate_index():
    # Define the path to the notes.md file
    notes_path = 'notes.md'  # Assuming notes.md is in the root directory
    
    # Read the existing index page
    with open(notes_path, 'r') as index_file:
        index_content = index_file.read()
    
    # Parse the content to extract existing links
    existing_links = [line.strip() for line in index_content.split('\n') if line.strip().startswith('- ')]
    
    # Scan the repository for Markdown files recursively
    markdown_files = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.md') and file != 'notes.md':
                markdown_files.append(os.path.relpath(os.path.join(root, file), start='.'))
    
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
    generate_index()



# The notes_path variable is set to 'notes.md', assuming that notes.md is in the root directory.
# The os.walk('.') function is used to recursively scan the current directory and its subdirectories for Markdown files.
# The start='.' parameter in os.path.relpath() ensures that the relative paths are calculated correctly relative to the root directory.