import difflib

def compare_text(file1, file2):
    """Shows line-by-line differences between two text files."""
    try:
        with open(file1) as f1, open(file2) as f2:
            diff = difflib.unified_diff(
                f1.readlines(), f2.readlines(),
                fromfile=file1, tofile=file2
            )
            for line in diff:
                print(line, end="")

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python text_diff.py <original_file> <modified_file>")
    else:
        compare_text(sys.argv[1], sys.argv[2])
