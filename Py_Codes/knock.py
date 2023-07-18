import time
from scapy.all import *

def knock_sequence(server_ip, ports):
    for port in ports:
        print(f"Knocking on port {port}...")
        packet = IP(dst=server_ip) / TCP(dport=port, flags="S")
        sr(packet, verbose=False)
        time.sleep(1)

if __name__ == "__main__":
    server_ip = "139.59.26.242"
    knocking_ports = [1000, 2000, 3000]  # Change these ports to your desired sequence

    knock_sequence(server_ip, knocking_ports)
