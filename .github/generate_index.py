import os

def generate_index():
    # Read the existing index page
    with open('notes.md', 'r') as index_file:
        index_content = index_file.read()
    
    # Parse the content to extract existing links
    existing_links = [line.strip() for line in index_content.split('\n') if line.strip().startswith('- ')]
    
    # Scan the repository for Markdown files
    markdown_files = [file for file in os.listdir() if file.endswith('.md') and file != 'notes.md']
    
    # Generate new links for Markdown files
    new_links = [f"- [{file.replace('.md', '')}](./{file})" for file in markdown_files]
    
    # Update the existing links with the new links
    updated_content = index_content
    for existing_link, new_link in zip(existing_links, new_links):
        updated_content = updated_content.replace(existing_link, new_link)
    
    # Write the updated content back to the index page
    with open('notes.md', 'w') as index_file:
        index_file.write(updated_content)

if __name__ == "__main__":
    generate_index()
