import csv
from ipregistry import IpregistryClient

# Function to read IP addresses from a text file
def read_ip_addresses(filename):
    with open(filename, 'r') as file:
        ip_addresses = file.read().strip().split('\n')
    return ip_addresses

# Function to perform IP lookup using ipregistry
def lookup_ips(ip_addresses, api_key):
    client = IpregistryClient(api_key)
    results = []
    for ip in ip_addresses:
        try:
            response = client.lookup_ip(ip)
            city = response.data.location.city
            state = response.data.location.region.code
            results.append((ip, city, state))
            print(f"Processed IP: {ip} - City: {city}, State: {state}")
        except Exception as e:
            print(f"Error processing IP {ip}: {str(e)}")
            results.append((ip, 'Error', 'Error'))  # Handle errors gracefully
    return results

# Function to save results to CSV file
def save_to_csv(results, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP', 'City', 'State'])
        writer.writerows(results)

# Function to save results to text file
def save_to_text(results, filename):
    with open(filename, 'w') as file:
        for result in results:
            file.write(f"IP: {result[0]}, City: {result[1]}, State: {result[2]}\n")

if __name__ == "__main__":
    input_file = "/ipwithnoports.txt"  # Replace with your input text file name
    output_csv_file = "/detailed_ips.csv"  # CSV file to save results
    output_text_file = "/detailed_ips.txt"  # Text file to save results
    api_key = "Your IP Registery API"  # Replace with your ipregistry API key

    # Step 1: Read IP addresses from input text file
    ip_addresses = read_ip_addresses(input_file)

    # Step 2: Perform IP lookup using ipregistry
    results = lookup_ips(ip_addresses, api_key)

    # Step 3: Save results to CSV and text files
    save_to_csv(results, output_csv_file)
    save_to_text(results, output_text_file)

    print("Process complete. Results saved to CSV and text files.")
