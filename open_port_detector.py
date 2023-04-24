import socket
import os 
# Define an array of high-risk ports you want to check and close if they're open
HIGH_RISK_PORTS = [22, 21, 23]

# Define a function to check if a given port is open
def is_port_open(port):
    try:
        # Create a socket object and attempt to connect to the port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect(('localhost', port))
        # If the connection is successful, the port is open
        HIGH_RISK_PORTS.append(port)
        return True
    except:
        # If the connection fails, the port is closed
        return False
    finally:
        # Close the socket
        s.close()

# Loop through all ports from 1 to 65535 and check if they're open
for port in range(1, 65536):
    if is_port_open(port):
   
        print(f"Port {port} is open")
	
        # If any high-risk port is open, close it
        if port in HIGH_RISK_PORTS:
            print(f"High-risk port {port} is open! Closing...")
            # Use firewall rules to close the high-risk port
            # For example, using the 'iptables' command:
            os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP")
            print("High-risk port closed")
        else:
            print("All port is now clouse your machine is safe")

