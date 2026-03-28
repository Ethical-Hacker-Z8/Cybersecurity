import random
import string
import hashlib
import base64
import socket

# -----------------------------
# Password Generator
# -----------------------------
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# -----------------------------
# SHA256 Hash Generator
# -----------------------------
def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# -----------------------------
# Base64 Encoder / Decoder
# -----------------------------
def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception:
        return "Invalid Base64 string!"

# -----------------------------
# Simple Port Scanner
# -----------------------------
def port_scanner(host, ports):
    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((host, port))
            open_ports.append(port)
        except:
            pass
        s.close()
    return open_ports

# -----------------------------
# Network Info
# -----------------------------
def network_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:
        print("\n=== Zohaib Cyber Security Toolkit ===")
        print("1. Generate Random Password")
        print("2. Generate SHA256 Hash")
        print("3. Base64 Encode")
        print("4. Base64 Decode")
        print("5. Simple Port Scanner")
        print("6. Network Info")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '1':
            length = int(input("Enter password length: "))
            print("Generated Password:", generate_password(length))

        elif choice == '2':
            text = input("Enter text to hash: ")
            print("SHA256 Hash:", generate_hash(text))

        elif choice == '3':
            text = input("Enter text to encode: ")
            print("Base64 Encoded:", base64_encode(text))

        elif choice == '4':
            text = input("Enter Base64 text to decode: ")
            print("Decoded Text:", base64_decode(text))

        elif choice == '5':
            host = input("Enter host/IP to scan: ")
            ports = input("Enter ports separated by comma (e.g., 21,22,80): ")
            ports = [int(p.strip()) for p in ports.split(',')]
            open_ports = port_scanner(host, ports)
            print("Open Ports:", open_ports if open_ports else "No open ports found")

        elif choice == '6':
            hostname, ip = network_info()
            print("Hostname:", hostname)
            print("IP Address:", ip)

        elif choice == '7':
            print("Exiting... Stay Secure!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()