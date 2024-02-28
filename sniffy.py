from scapy.all import *
import os

from scapy.plist import PacketList


def new_sniff() -> object:
    print("start new sniffing session...")
    # params
    count = input('Please enter number of packets to capture [0=infinity]: ')
    timeout = input('Please enter time for sniffing [in seconds]: ')

    print("Sniffing...please wait")
    pkts = sniff(count=int(count), timeout=int(timeout))

    save_packets(pkts)
    return pkts


def save_packets(pkts):
    if os.path.exists("pkts.cap"):
        try:
            os.remove("pkts.cap")
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

    wrpcap("pkts.cap", pkts)


def packets_size(pkts):
    size = 0
    for pckt in pkts:
        if 'IP' in pckt:
            size = size + pckt['IP'].len
    return size


def tcp_packets_count(pkts):
    count = 0
    for pckt in pkts:
        if 'TCP' in pckt:
            count = count + 1
    return count


def udp_packets_count(pkts):
    count = 0
    for pckt in pkts:
        if 'UDP' in pckt:
            count = count + 1
    return count


def icmp_packets_count(pkts):
    count = 0
    for pckt in pkts:
        if 'ICMP' in pckt:
            count = count + 1
    return count


def arp_packets_count(pkts):
    count = 0
    for pckt in pkts:
        if 'ARP' in pckt:
            count = count + 1
    return count


def main() -> object:
    """

    :rtype: object
    """
    # Start Sniffing Script
    new_session = input("New Sniffing session or Read last pCap file? [new/read]: ")

    if new_session == 'new':
        pkts = new_sniff()
    elif new_session == 'read':
        print('\nReading pCap file...Wait!')
        if os.path.exists("pkts.cap"):
            pkts = rdpcap("pkts.cap")
        else:
            print("pCap file not exists...\n")
            pkts = new_sniff()
    else:
        pkts: PacketList = new_sniff()

    # statistics
    print("\nStatistics:")
    print("Total Packets Sniffed: " + str(len(pkts)))
    print("Total Packets Size [Network Layer - IP]: " + str(packets_size(pkts)) + ' bytes')
    print("Sniffed TCP: " + str(tcp_packets_count(pkts)) + " packets")
    print("Sniffed UDP: " + str(udp_packets_count(pkts)) + " packets")
    print("Sniffed ICMP: " + str(icmp_packets_count(pkts)) + " packets")
    print("------------------")
    print("Sniffed ARP: " + str(arp_packets_count(pkts)) + " packets")
    print('\n' + 'Packets List:')
    pkts.show()

    while 1:
        index = input('\nWhich packet you want to see? [type exit for end]\n')
        if index == 'exit':
            break
        elif isinstance(int(index), int):
            packet1: object = pkts[int(index)]
            packet1.show()


main()
