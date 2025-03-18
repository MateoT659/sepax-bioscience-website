# removes whitespace from inquire html

import sys

def flatten_html(html_content):
    # Remove newlines and tabs
    html_content = html_content.replace('\t', '').replace('  ', '')   
    # Remove multiple spaces and newlines
    return html_content.strip()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python flatten.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            html_content = file.read()
        
        flattened_content = flatten_html(html_content)
        
        with open('out.html', 'w') as output_file:
            output_file.write(flattened_content)
        
        print("Flattened content written to out.html")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
# Example usage: python flatten.py input.html
