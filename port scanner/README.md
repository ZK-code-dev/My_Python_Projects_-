🛡️ Port Scanner

Purpose: Scan a range of ports on a given IP address or hostname to find which ports are open.

⚠️ Disclaimer: This tool is intended for educational purposes only.
Only scan devices or networks that you own or have explicit permission to test.
Safe targets for learning include your localhost (127.0.0.1) or publicly legal test servers like nmap ScanMe
.

This tool can help you check network security or see which services are running on a machine. ⚡

🕹 How to Use

Run the script. You will be prompted to enter:

Target IP or hostname 🌐

Start port (integer between 1–65535)

End port (integer between 1–65535)

The script will scan all ports in the given range and display open ports:

[OPEN] Port 22 is open.
[OPEN] Port 80 is open.

Results are also saved in a log file: port_results.log 📝

💡 How the Code Works
1️⃣ User Input & Validation

Prompts the user for target address and port range.

.strip() removes extra whitespace from inputs.

Validates:

Target IP/hostname using socket.gethostbyname() 🌐

Port numbers: integers between 1–65535 and start ≤ end.

Invalid input exits the program with an error message. ❌

Comments in the code explain may name sections/steps, give a brief explantion of a step or may just be my notes.
2️⃣ Logging

Uses Python’s logging module to save open ports to a file: port_results.log.

File permissions are set (if supported) so owner can read/write and group can read. 🔐

3️⃣ Scanning Ports

Loops through the port range with for port in range(scan_start_port, scan_end_port + 1).

Creates a socket object using socket.socket() and sets a timeout of 1 second. ⏱️

Uses connect_ex() to attempt connection:

Returns 0 if the port is open ✅

Logs open ports and prints them to the console.

with statement ensures sockets are closed properly after each test.

Comments in the code show step-by-step explanation of the scanning loop, including why we use with and connect_ex(). Some comments are also there to explain the “first idea” or important steps for beginners. 📝

4️⃣ Completion

Prints a final message showing that the scan is complete.

Open ports are saved in the log file for later reference. 🗂️

🖥 Example Usage
Enter targeted IP address or hostname: 127.0.0.1
Enter the start port: 20
Enter the end port: 25

Scanning ports 20 to 25 on 127.0.0.1...

[OPEN] Port 22 is open.
[OPEN] Port 23 is open.

Completed port scan successfully! Results saved to: port_results.log

⚙️ Features

Validates IP addresses and hostnames 🌐

Validates port ranges and input types 🔢

Timeout for each port prevents hanging ⏱️

Logs open ports to a file 📄

Friendly and detailed print messages for user clarity 💡

📌 Notes

Comments in the code help explain why each step exists, such as validating input, looping through ports, and logging results.

Some comments show earlier ideas or expanded explanations, which are useful for learning or understanding the flow of the program. ✨

Can be extended with features like multi-threaded scanning, exporting logs in different formats, or scanning common service ports automatically. 🚀

🎉 Use this script to safely explore open ports on your own network and learn about network security! 🔍🖥️
