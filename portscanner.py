
import socket

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((ip, port))
    s.close()
    return result == 0

def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        s.connect((ip, port))
        banner = s.recv(1024)
        s.close()
        return banner.decode("utf-8").strip()
    except:
        return None

ip = input("target IP: ")
open_ports = []

for port in range(1, 1024):
    if scan_port(ip, port):
        banner = grab_banner(ip, port)
        if banner:
            print(f"[OPEN] {port} -> {banner}")
        else:
            print(f"[OPEN] {port}")
        open_ports.append(port)

print(f"\nopen ports: {open_ports}")
print(f"\total open ports: {len(open_ports)}")

with open("port_result.txt", "w") as f:
    f.write("port scanning result\n")
    f.write(f"target IP: {ip}\n\n")
    for i in open_ports:
        f.write(f"[OPEN] {i}\n")
    f.write(f"total {len(open_ports)} ports\n")

print("saved port_result.txt")


