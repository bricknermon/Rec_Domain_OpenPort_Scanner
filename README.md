# domain_port_scanner
Simple csv input, csv output recursive open port scanner of domain and subdomains. Output in digestible/concise format : ).

-------------------------------------------------------------------------------------------------------------------------------------

### Setup and configurations : 
Expected input file format (output file is created or updated once execution is completed):

![file_format](https://github.com/bricknermon/domain_port_scanner/assets/94518180/809bbfd2-76af-4fb0-b3d8-9456e16250c3)

What to configure within either file:

![image](https://github.com/bricknermon/domain_port_scanner/assets/94518180/3c5f2731-fd3f-4645-b8bb-94a672fe7ac5)

Revise ```main('tester.csv', 'scan_results.csv')``` to your files where 

```main('inputFilename.csv', 'desiredOutputFileName.csv')```

-------------------------------------------------------------------------------------------------------------------------------------

![image](https://github.com/bricknermon/domain_port_scanner/assets/94518180/6f0fd34d-5f88-4385-9aa5-30a7ca0dc6a9)

[port_scan_2Col.py](https://github.com/bricknermon/domain_port_scanner/blob/main/port_scan_2Col.py)

**Cmd to Run:** ```sudo python3 port_scan.py inputFileName.csv arbitaryName.csv```

Example cmd: ```sudo python3 port_scan.py tester.csv scan_results.csv```

-------------------------------------------------------------------------------------------------------------------------------------

![image](https://github.com/bricknermon/domain_port_scanner/assets/94518180/9a4cdc31-fdbf-434b-95fb-c4fddda84a05)

[port_scan_multCol.py](https://github.com/bricknermon/domain_port_scanner/blob/main/port_scan_multCol.py)

**Cmd to Run:** ```sudo python3 port_scan.py inputFileName.csv arbitaryName.csv```

Example cmd: ```sudo python3 port_scan.py tester.csv scan_results.csv```
