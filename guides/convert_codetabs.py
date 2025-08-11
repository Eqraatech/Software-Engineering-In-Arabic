#!/usr/bin/env python3
import os
import re
import glob
import json

def extract_codetabs_content(content):
    """Extract content between <CodeTabs> tags"""
    start_pattern = r'<CodeTabs snippets={'
    end_pattern = r'} />'
    
    start_idx = content.find(start_pattern)
    if start_idx == -1:
        return None, content
    
    # Find the matching closing bracket
    bracket_count = 0
    search_start = start_idx + len(start_pattern) - 1  # Position at the opening bracket
    
    for i in range(search_start, len(content)):
        if content[i] == '{':
            bracket_count += 1
        elif content[i] == '}':
            bracket_count -= 1
            if bracket_count == 0:
                end_idx = i + len(end_pattern) - 1
                codetabs_content = content[start_idx:end_idx + 1]
                return codetabs_content, content
    
    return None, content

def parse_snippets_array(snippets_str):
    """Parse the snippets array from the CodeTabs component"""
    # Clean up the string
    snippets_str = snippets_str.strip()
    if not snippets_str.startswith('['):
        return []
    
    snippets = []
    i = 1  # Skip opening bracket
    while i < len(snippets_str):
        if snippets_str[i] == '{':
            # Find the end of this object
            bracket_count = 0
            start = i
            for j in range(i, len(snippets_str)):
                if snippets_str[j] == '{':
                    bracket_count += 1
                elif snippets_str[j] == '}':
                    bracket_count -= 1
                    if bracket_count == 0:
                        obj_str = snippets_str[start:j+1]
                        snippet = parse_snippet_object(obj_str)
                        if snippet:
                            snippets.append(snippet)
                        i = j + 1
                        break
        else:
            i += 1
    
    return snippets

def parse_snippet_object(obj_str):
    """Parse a single snippet object"""
    # Extract language
    lang_match = re.search(r'language:\s*[\'\"]([^\'\"]*)[\'\".]', obj_str)
    language = lang_match.group(1) if lang_match else 'text'
    
    # Extract label
    label_match = re.search(r'label:\s*[\'\"]([^\'\"]*)[\'\".]', obj_str)
    label = label_match.group(1) if label_match else ''
    
    # Extract code (this is the tricky part due to backticks)
    code_match = re.search(r'code:\s*`([^`]*(?:`[^`][^`]*)*)`', obj_str, re.DOTALL)
    if not code_match:
        # Try alternative pattern for multiline code
        code_match = re.search(r'code:\s*`([\s\S]*?)`(?=\s*,\s*label)', obj_str)
    
    if code_match:
        code = code_match.group(1)
        # Clean up the code
        code = code.replace('\\n', '\n')
        code = code.replace('\\`', '`')
        code = code.replace('\\\\', '\\')
        code = code.strip()
        
        return {
            'language': language,
            'code': code,
            'label': label
        }
    
    return None

def convert_codetabs_to_markdown(content):
    """Convert CodeTabs components to standard markdown code blocks"""
    # Remove import statement
    content = re.sub(r'^import CodeTabs from.*$\n?', '', content, flags=re.MULTILINE)
    
    # Process all CodeTabs instances
    while True:
        codetabs_content, content = extract_codetabs_content(content)
        if not codetabs_content:
            break
        
        # Extract the snippets array
        snippets_match = re.search(r'<CodeTabs snippets=\{(\[.*\])\} />', codetabs_content, re.DOTALL)
        if not snippets_match:
            # Remove the codetabs content if we can't parse it
            content = content.replace(codetabs_content, '')
            continue
        
        snippets_str = snippets_match.group(1)
        snippets = parse_snippets_array(snippets_str)
        
        # Convert to markdown code blocks
        markdown_blocks = []
        for snippet in snippets:
            if snippet and snippet['code']:
                if snippet['label'] and snippet['label'] != snippet['language']:
                    markdown_blocks.append(f"<!-- {snippet['label']} -->\n```{snippet['language']}\n{snippet['code']}\n```")
                else:
                    markdown_blocks.append(f"```{snippet['language']}\n{snippet['code']}\n```")
        
        replacement = '\n\n'.join(markdown_blocks)
        content = content.replace(codetabs_content, replacement)
    
    # Clean up extra whitespace
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    return content

def main():
    # Find all .md files
    md_files = glob.glob('/Users/mahyoussef/repos/In-a-Nutshell/guides/**/*.md', recursive=True)
    
    files_processed = 0
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file contains CodeTabs
            if 'CodeTabs' in content:
                converted_content = convert_codetabs_to_markdown(content)
                
                # Only write if content changed
                if converted_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(converted_content)
                    
                    files_processed += 1
                    print(f'Processed: {os.path.basename(file_path)}')
        
        except Exception as e:
            print(f'Error processing {file_path}: {e}')
    
    print(f'\nTotal files processed: {files_processed}')

if __name__ == '__main__':
    main()

