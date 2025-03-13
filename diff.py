import hashlib

def hash_file(filepath):
    """Returns the SHA-256 hash of a given file."""
    try:
        hasher = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError as e:
        print(f"❌ Error: {filepath} not found!")
        return "" # empty string

def compare_files(file1, file2):
    """Compares two files by their SHA-256 hashes."""
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    if not hash1 or not hash2:
        return

    print(f"Original Hash: {hash1}")
    print(f"Modified Hash: {hash2}")

    if hash1 == hash2:
        print("✅ Files are identical.")
    else:
        print("❌ Files have been modified.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python diff.py <original_file> <modified_file>")
    else:
        compare_files(sys.argv[1], sys.argv[2])
