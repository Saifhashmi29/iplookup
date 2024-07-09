import ipaddress

# File paths
input_file = '/home/linux/Desktop/iplook/ipports.txt'
output_file = '/home/linux/Desktop/iplook/ipwithnoports.txt'

# Function to remove network prefix and save IP addresses
def process_ip_addresses(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            for line in f_in:
                line = line.strip()  # Remove any surrounding whitespace
                if line:
                    # Split by '/', take only the first part which is the IP address
                    ip_string = line.split('/')[0]
                    try:
                        # Validate and normalize the IP address
                        ip = ipaddress.ip_address(ip_string)
                        # Write the IP address to the output file
                        f_out.write(str(ip) + '\n')
                    except ValueError as e:
                        print(f"Invalid IP address: {ip_string}, Error: {e}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

# Call the function to process IP addresses
process_ip_addresses(input_file, output_file)

print(f"Modified IP addresses saved to '{output_file}'.")
