"""
device.py

Defines the Device class used throughout LANGuard.
Each Device represents one discovered network host.
"""


class Device:

    def __init__(self, IP: str, MAC: str):

        self.IP = IP

        self.MAC = MAC

        self.Vendor = ""

        self.Status = ""