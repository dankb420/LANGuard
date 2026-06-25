"""
scanner.py

Responsible for discovering devices on the LAN.
"""

from scapy.all import ARP, Ether, srp, conf, get_if_addr
import ipaddress
from device import Device
from config import INTERFACE

class Scanner:

    def __init__(self):
        pass

    def ScanNetwork(self) -> list[Device]:
        local_ip = get_if_addr(INTERFACE)
        network = ipaddress.ip_network(f"{local_ip}/24", strict=False)
        target = str(network)
        print(target) #TEMPORARY DEBUGGING
        arp = ARP(pdst=target)

        ethernet = Ether(dst="ff:ff:ff:ff:ff:ff")

        packet = ethernet / arp

        answered, _ = srp(
            packet,
            iface=INTERFACE,
            timeout=2,
            retry=1,
            verbose=False
         )
        devices = []

        for _, received in answered:

            device = Device(received.psrc, received.hwsrc)

            devices.append(device)

        return devices