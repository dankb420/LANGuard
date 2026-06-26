"""
scanner.py

Responsible for discovering devices on the LAN.
"""

from scapy.all import (
    ARP,
    Ether,
    srp,
    get_if_addr,
    get_if_list
)
from config import INTERFACE, SCAN_TIMEOUT
import ipaddress
from device import Device
class Scanner:

    def __init__(self):
        pass
    def GetInterface(self):

        if INTERFACE != "AUTO":
            return INTERFACE

        for interface in get_if_list():

            try:

                ip = get_if_addr(interface)

                if (
                    ip != "127.0.0.1"
                    and ip != "0.0.0.0"
                    and not ip.startswith("169.254.")
                ):
                    return interface

            except Exception:
                pass

        raise RuntimeError("No active network interface found.")

    def ScanNetwork(self) -> list[Device]:
        interface = self.GetInterface()
        local_ip = get_if_addr(interface)
        network = ipaddress.ip_network(f"{local_ip}/24", strict=False)
        target = str(network)
        print(target) #TEMPORARY DEBUGGING
        arp = ARP(pdst=target)

        ethernet = Ether(dst="ff:ff:ff:ff:ff:ff")

        packet = ethernet / arp

        answered, _ = srp(
            packet,
            iface=interface,
            timeout=SCAN_TIMEOUT,
            retry=1,
            verbose=False
         )
        devices = []

        for _, received in answered:

            device = Device(received.psrc, received.hwsrc)

            devices.append(device)

        return devices