import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_large_file(filename, size_in_mb):
    target_size = size_in_mb * 1024 * 1024  # Convert MB to bytes
    chunk_size = 1024  # 1KB chunks

    with open(filename, 'w') as file:
        current_size = 0
        while current_size < target_size:
            chunk = generate_random_string(chunk_size)
            file.write(chunk + '\n')
            current_size += len(chunk) + 1  # +1 for newline character

    print(f"File '{filename}' of approximately {size_in_mb}MB has been generated.")

# Generate a 10MB file
generate_large_file('large_file.txt', 10)