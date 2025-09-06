from scapy.all import sniff, IP, TCP, UDP, ICMP, wrpcap

file = "found_packets.pcap"
found = []

def callback(packet):
    return

def main():
    try: 
        sniff(prn=callback,store=False)
    except KeyboardInterrupt:
        if found:
            wrpcap(file,found)


if __name__ == "__main__":
    main()

