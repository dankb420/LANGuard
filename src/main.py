from scanner import Scanner
from database import Database
from detector import Detector
from vendor import Vendor


def Main():

    scanner = Scanner()

    database = Database()

    detector = Detector()

    vendor = Vendor()

    current_devices = scanner.ScanNetwork()

    previous_devices = database.Load()

    new_devices = detector.Detect(previous_devices, current_devices)

    database.Save(current_devices)

    print(f"Current Devices: {len(current_devices)}")
    print(f"Previous Devices: {len(previous_devices)}")
    print(f"New Devices: {len(new_devices)}\n")

    print("Discovered Devices\n")

    for device in current_devices:

        print(
            f"{device} | {vendor.GetVendor(device.MAC)}"
        )


if __name__ == "__main__":
    Main()