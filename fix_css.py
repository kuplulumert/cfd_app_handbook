import os
import re

def fix_css_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if file has the malformed CSS pattern
    if 'background-color: #f7fafc;' in content and '@keyframes fadeInPage' in content:
        print(f"Fixing CSS in {filepath}...")
        
        # Fix body CSS block
        body_pattern = r'body\s*\{[^}]*background-color:\s*#f7fafc;[^}]*\}'
        
        # Create the correct body CSS
        correct_body_css = '''body {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #2d3748;
            background-color: #f7fafc;
            min-height: 100vh;
            opacity: 0;
            animation: fadeInPage 1.2s ease-out forwards;
            overflow-x: hidden;
        }'''
        
        # First, try to fix any malformed body block
        if re.search(r'@keyframes fadeInPage.*\{[^}]*\}.*min-height: 100vh', content, re.DOTALL):
            # Extract keyframes separately
            keyframes_css = '''
        @keyframes fadeInPage {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }'''
            
            # Remove malformed body block and keyframes
            content = re.sub(r'body\s*\{[^}]*background-color:\s*#f7fafc;.*?\}(\s*@keyframes fadeInPage.*?\}.*?min-height: 100vh;.*?overflow-x: hidden;\s*\})?', correct_body_css + keyframes_css, content, flags=re.DOTALL)
        
        # Remove duplicate properties
        content = re.sub(r'(box-shadow:[^;]+;)\s*\1', r'\1', content)
        
        # Remove duplicate closing braces
        content = re.sub(r'\}\s*\}(\s*\.)', r'}\n\n        \1', content)
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed {filepath}")
    else:
        print(f"No issues found in {filepath}")

# Fix all model pages
model_files = [f for f in os.listdir('models/') if f.endswith('.html') and 'backup' not in f and 'corrupted' not in f and 'correct' not in f and 'wrong' not in f]

for model_file in model_files:
    filepath = f"models/{model_file}"
    fix_css_file(filepath)

# Also fix main pages
main_pages = ['time-dependency.html', 'methods.html', 'product-guide.html']
for page in main_pages:
    if os.path.exists(page):
        fix_css_file(page)

print("CSS fix complete!")
