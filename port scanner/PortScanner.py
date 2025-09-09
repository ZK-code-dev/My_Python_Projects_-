# =============================================
# File Name: PortScanner.py
# Purpose: Scan a range of ports on a given IP/hostname to find open ports
# =============================================

import socket  # create and manage network connections (like scanning ports)
from datetime import datetime  # datetime module to record the time of the scan
import logging  # logging module to log the results of the port scan
import os  # os module to manage file permissions and paths

# Step 1: Create needed variables and input options
target_address = input("Enter targeted IP address or hostname: ").strip()
# .strip() removes whitespace's from start and end of user input.
scan_start_port = input("Enter the start port: ").strip()
scan_end_port = input("Enter the end port: ").strip()
# One second timeout for each port scan
port_timeout = 1

# Step 2: Verify user input.


# function to validate IP address or hostname
def validate_ip_or_hostname(address):
    try:
        socket.gethostbyname(address)
        return True
    except socket.error:
        return False


"""  Converts hostname to IP address,
    returns True if successful. 
    Will raise an error if the address is invalid (socket.error) returns False."""


if not target_address or not validate_ip_or_hostname(target_address):
    print("Error, invalid IP address or hostname. Exiting program!")
    exit()
    # If the input is empty or invalid, print error message first then exits the program.

try:
    scan_start_port = int(scan_start_port)
    scan_end_port = int(scan_end_port)
    if scan_start_port < 1 or scan_end_port > 65535 or scan_start_port > scan_end_port:
        raise ValueError
except ValueError:
    print("Error, Invalid port range. Exiting program!")
    exit()
    """ try will start a block of code that may raise an error.
      int() converts the input strings to integers.
      if is used to see if the next following conditions are True and will raise ValueError.
      The except block catches the ValueError if the input is not a valid integer or if the port range is invalid.
    """

# Step 3: Create secure results log file
# Define the log file path in a variable.
log_file_path = "port_results.log"
logging.basicConfig(                          # Setup the logging configuration ( used the logging module)
    filename=log_file_path,
    format='%(asctime)s - %(message)s',
    level=logging.INFO)

# Applying file permissions to the log file
try:
    # Owner can read/write, group can read only.
    os.chmod(log_file_path, 0o644)
except:
    pass  # does nothing if error occurs while changing permissions like non-existing file,
    # or windows doesn't support chmod.

# Step 4: Loop through and test all selected ports
print(
    f"\nScanning ports {scan_start_port} to {scan_end_port} on {target_address}...\n")
for port in range(scan_start_port, scan_end_port + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(port_timeout)
        result = s.connect_ex((target_address, port))
        if result == 0:
            print(f"[OPEN] Port {port} is open.")
            logging.info(f"Open Port found on {target_address}: Port {port}")

        """       First we used the print function to display the scanning message.
                  then we looped through the range of ports from start to end.
                        We created a socket object using the socket module.
                        We set a timeout for the socket connection to avoid long waits.
                        We used connect_ex() to attempt to connect to the target address and port.
                        If the result is 0, it means the port is open, and we log it.
                        The with statement ensures that the socket is properly closed after use.
                        Then we print the results to the console."""


# Step 5: Finalize scans and close resources.
print(f"\nCompleted port scan successfully! Results saved to: {log_file_path}")
