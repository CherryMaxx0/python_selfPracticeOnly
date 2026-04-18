import hashlib
import os

def hash_text_sha256(text):
    hash_object = hashlib.sha256(text.encode('utf-8'))
    return hash_object.hexdigest()

def hash_file_sha256(filepath):
    if not os.path.isfile(filepath):
        return "File not found!"
    
    hash_object = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def main():
    print("=== SHA-256 Hash Generator ===")
    print("1. Hash text")
    print("2. Hash file")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        text = input("Enter text to hash: ")
        print("SHA-256 Hash:\n", hash_text_sha256(text))
    elif choice == "2":
        file_path = input("Enter full path to the file: ")
        result = hash_file_sha256(file_path)
        print("SHA-256 Hash:\n", result)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
