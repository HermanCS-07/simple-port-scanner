import socket  # allows us to communicate with other machines using TCP and UDP
import termcolor  # print statements in different colors


def scan(target, ports):
    print("\nScanning: " + str(target))
    for port in range(1, int(ports) + 1):  # scans the target and its ports
        scan_port(target, port)


def scan_port(ip_addr, port):  # where the scan happens
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # assigns the socket() object to var 'sock'
        sock.connect((ip_addr, port))
        print(termcolor.colored(("[+] Port is Open: " + str(port)), 'green'))
        sock.close()
    except:
        #print("Port is Closed: " + str(port))
        pass


if __name__ == '__main__':
    targets = input("[*] Enter Target to Scan (split by ,): ")
    ports = int(input("[*] Enter no. of Ports to Scan: "))

    if ',' in targets:
        print(termcolor.colored(("[*] Scanning Multiple Targets..."), 'yellow'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(), ports)
    else:
        scan(targets.strip(), ports)
