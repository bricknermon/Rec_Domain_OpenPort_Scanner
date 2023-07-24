# domain_port_scanner

This project is a robust, efficient port scanner designed for scanning domains and their subdomains. It accepts a CSV file as input, containing the list of domains to be scanned, and generates an output CSV file detailing the open ports found for each domain. Our scanner's output is meticulously organized, ensuring that the results are concise, easy to interpret, and ready for further analysis. This tool is perfect for those who require a straightforward, yet in-depth understanding of their domain's open ports

-------------------------------------------------------------------------------------------------------------------------------------

## Setup and configurations : 


**Required instillation**

Install nmap ```pip install python-nmap``` 

-------------------------------------------------------------------------------------------------------------------------------------

### **Expected input file format (output file is created or updated once execution is completed):**

Csv file in following format, one domain per row:

domain1.com

domain2.com

domain3.com
...

![file_format](https://github.com/bricknermon/domain_port_scanner/assets/94518180/809bbfd2-76af-4fb0-b3d8-9456e16250c3)

-------------------------------------------------------------------------------------------------------------------------------------

### **What to configure within either file:**

Navigate to the bottom of your desired output file. it should look like below:

![image](https://github.com/bricknermon/domain_port_scanner/assets/94518180/3c5f2731-fd3f-4645-b8bb-94a672fe7ac5)

Revise the following ```main('tester.csv', 'scan_results.csv')``` 

to your file names where 

```main('inputFilename.csv', 'desiredOutputFileName.csv')```

-------------------------------------------------------------------------------------------------------------------------------------

### Example Run of 2Col output

![image](https://github.com/bricknermon/domain_port_scanner/assets/94518180/6f0fd34d-5f88-4385-9aa5-30a7ca0dc6a9)

[port_scan_2Col.py](https://github.com/bricknermon/domain_port_scanner/blob/main/port_scan_2Col.py)

**Cmd to Run:** ```sudo python3 port_scan_2Col.py inputFileName.csv arbitaryName.csv```

Example cmd: ```sudo python3 port_scan_2Col.py tester.csv scan_results.csv```

-------------------------------------------------------------------------------------------------------------------------------------

### Example Run of Multi Col Output

![image](https://github.com/bricknermon/domain_port_scanner/assets/94518180/9a4cdc31-fdbf-434b-95fb-c4fddda84a05)

[port_scan_multCol.py](https://github.com/bricknermon/domain_port_scanner/blob/main/port_scan_multCol.py)

**Cmd to Run:** ```sudo python3 port_scan_multCol.py inputFileName.csv arbitaryName.csv```

Example cmd: ```sudo python3 port_scan_multCol.py tester.csv scan_results.csv```

-------------------------------------------------------------------------------------------------------------------------------------




> [!] legal disclaimer : Usage of this script for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
