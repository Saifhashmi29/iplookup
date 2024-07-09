import csv

# File paths
csv_file = '/detailed_ips.csv'
txt_file = '/cities.txt'
output_file = '/Target_citites_with_ips.csv'

# Function to read city names from text file
def read_city_names(txt_file):
    try:
        with open(txt_file, 'r') as f:
            cities = [line.strip() for line in f]
        return cities
    except FileNotFoundError:
        print(f"Error: File '{txt_file}' not found.")
        return []

# Function to search and filter records based on city names
def filter_records(csv_file, cities, output_file):
    try:
        with open(csv_file, 'r', newline='') as csv_in, open(output_file, 'w', newline='') as csv_out:
            reader = csv.DictReader(csv_in)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                city = row['City'].strip()
                if city in cities:
                    writer.writerow(row)
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return

# Main process
def main():
    # Read city names from text file
    cities = read_city_names(txt_file)

    if cities:
        # Filter records based on city names and save to output CSV file
        filter_records(csv_file, cities, output_file)
        print(f"Filtered records saved to '{output_file}'.")

if __name__ == "__main__":
    main()
