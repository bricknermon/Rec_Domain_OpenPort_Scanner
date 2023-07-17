import csv
import concurrent.futures
import nmap
import socket

def resolve_host(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

def scan_ports(domain):
    nm = nmap.PortScanner()

    host = resolve_host(domain)
    if host is None:
        return None

    # Print a message indicating the domain that is being scanned
    print(f"Scanning domain: {domain}")
    
    # Perform the port scan, scanning only the top 1000 most common ports
    nm.scan(host, arguments='-sS -T4 --max-retries 1')  # Stealth SYN scan with retries

    scan_results = []
    if host in nm.all_hosts():  # Check if the host is in the scan result
        for protocol in nm[host].all_protocols():
            for port in nm[host][protocol].keys():
                r = nm[host][protocol][port]
                scan_results.append(f"{port}/{protocol}/{r['state']}/{r['name']}")

    return domain, "; ".join(scan_results)

def main(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as file:
        domains = [line.strip() for line in file]

    # Process each domain
    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        scan_results = list(executor.map(scan_ports, domains))
        for result in scan_results:
            if result is not None:
                results.append(result)

    # Write the output file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Domain', 'Scan Results'])
        writer.writerows(results)

# Run the main function
if __name__ == "__main__":
    main('tester.csv', 'scan_results.csv')
