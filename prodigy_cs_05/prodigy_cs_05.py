from scapy.all import sniff, IP, TCP, UDP

def packetCallback(packet):
    if IP in packet:
        ipSrc = packet[IP].src
        ipDest = packet[IP].dst
        protocol = packet[IP].proto

        if protocol == 6:  
            if TCP in packet:
                sPort = packet[TCP].sPort
                dPort = packet[TCP].dPort
                print(f"TCP Packet: {ipSrc}:{sPort} ---> {ipDest}:{dPort}")
        elif protocol == 17:  
            if UDP in packet:
                sPort = packet[UDP].sPort
                dPort = packet[UDP].dPort
                print(f"UDP Packet: {ipSrc}:{sPort} ---> {ipDest}:{dPort}")
        else:
            print(f"Other IP Packet: {ipSrc} ---> {ipDest} (Protocol: {protocol})")

def main():
    print("Network Analyzer")
    sniff(filter="ip", prn=packetCallback, store=0)

if __name__ == "__main__":
    main()
