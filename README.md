# iplookup
This is a python project to fetch details (Cities and State ) of ipv4 addresses present in txt file using ipregistery repository on github.


# Overview
This Python project fetches details of IPv4 addresses from a list using the ipregistry repository and stores the information in CSV files. It consists of three main parts:

IP Address Normalization: Cleans up IP addresses extracted from a file by removing port numbers.
IP Lookup and CSV Generation: Utilizes the ipregistry API to fetch city and state information for each IP address, saving results in a detailed CSV and text file.
Filtering by Cities: Filters detailed IP information based on a list of specified cities in the United States, saving relevant records to a separate CSV file.

# Project Structure

 /iplook/
│
├── ip_addr.txt                  # Initial file with IP addresses including ports
├── ipwithnoports.txt            # Cleaned-up file with IP addresses (no ports)
├── detailed_ips.csv             # Detailed IP information (IP, City, State)
├── detailed_ips.txt             # Detailed IP information (text format)
├── cities.txt                   # List of US cities for filtering
├── Target_cities_with_ips.csv   # Filtered IP information based on cities
│
├── remove_ports.py             # Python script for IP address normalization
├── ipdetails_fetch_from_ipregistry.py                 # Python script for IP lookup and CSV generation
└── city_filter.py               # Python script for filtering IP information by cities

# Usage
Prerequisites
Python 3.x installed
Required Python packages (ipaddress, ipregistry, csv)
Setup
Clone the repository:

git clone https://github.com/your-username/iplookup.git
cd iplookup

# Install dependencies:


pip install -r requirements.txt
Obtain an API key from ipregistry and replace 'Your IP Registery API' in ipdetails_fetch_from_ipregistry.py with your actual API key.

# Execution
Normalize IP Addresses:

python ip_processing.py

# Fetch IP Details and Generate Files:


python ip_lookup.py

# Filter IP Details by Cities:

python city_filter.py

# Notes
Ensure your input files (ip_addr.txt and cities.txt) are correctly formatted as specified.
Review API usage limits and guidelines from ipregistry.

#License
Free for all!! Enjoy!
