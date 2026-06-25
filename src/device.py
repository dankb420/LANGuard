"""
device.py

Defines the Device class used throughout LANGuard.
Each Device represents one discovered network host.
"""


class Device:

    def __init__(self, IP: str, MAC: str):

        self.IP = IP
        self.MAC = MAC

    def __str__(self) -> str:

        return f"{self.IP} ({self.MAC})"