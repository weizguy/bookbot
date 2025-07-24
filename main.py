import sys
from stats import create_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    create_report(book_text)
    
main()