"""
detector.py

Responsible for detecting new devices.
"""

from device import Device


class Detector:

    def __init__(self):
        pass


    def Detect(
        self,
        previous_devices: list[Device],
        current_devices: list[Device]
    ) -> list[Device]:

        known_macs = set()

        new_devices = []

        for device in previous_devices:

            known_macs.add(device.MAC)

        for device in current_devices:

            if device.MAC not in known_macs:

                new_devices.append(device)

        return new_devices