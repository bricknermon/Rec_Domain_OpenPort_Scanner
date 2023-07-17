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

    ports, protocols, states, services = [], [], [], []
    if host in nm.all_hosts():  # Check if the host is in the scan result
        for protocol in nm[host].all_protocols():
            for port in nm[host][protocol].keys():
                r = nm[host][protocol][port]
                ports.append(str(port))
                protocols.append(protocol)
                states.append(r['state'])
                services.append(r['name'])
                
    if ports:
        return domain, ', '.join(ports), ', '.join(protocols), ', '.join(states), ', '.join(services)

def main(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as file:
        domains = [line.strip() for line in file]

    # Process each domain
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(scan_ports, domains))

    # Filter out None results
    results = [result for result in results if result is not None]

    # Write the output file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Domain', 'Open Ports', 'Protocols', 'States', 'Services'])
        writer.writerows(results)

# Run the main function
if __name__ == "__main__":
    main('tester.csv', 'scan_results.csv')
