# Initialize a set to store unique destination IP addresses
unique_dst_ips = set()

# Read the records from the "rupa.txt" file
input_file = "rupa.txt"

try:
    with open(input_file, "r") as file:
        records = file.readlines()
except FileNotFoundError:
    print(f"File '{input_file}' not found. Make sure the file exists.")
    exit(1)

# Parse through the records and extract unique destination IP addresses
for record in records:
    parts = record.split()
    for part in parts:
        if part.startswith("dst="):
            # Extract the destination IP address and add it to the set
            dst_ip = part.split("=")[1]
            unique_dst_ips.add(dst_ip)

# Count the number of unique destination IP addresses
num_unique_dst_ips = len(unique_dst_ips)

# Print the count of unique destination IP addresses
print(f"Number of unique destination IP addresses: {num_unique_dst_ips}")
