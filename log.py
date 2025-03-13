import datetime
from diff import hash_file

def log_hash(file):
    """Logs the hash of a file to hash_log.txt."""
    hash_value = hash_file(file)
    if not hash_value:
        return

    with open("hash_log.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} - {file}: {hash_value}\n")

    print(f"📜 Hash logged for {file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python log.py <file_to_log>")
    else:
        log_hash(sys.argv[1])
