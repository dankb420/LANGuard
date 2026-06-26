from scanner import Scanner
from database import Database
from detector import Detector
from vendor import Vendor


def RunLANGuard():

    scanner = Scanner()

    database = Database()

    detector = Detector()

    vendor = Vendor()

    current_devices = scanner.ScanNetwork()

    previous_devices = database.Load()

    new_devices = detector.Detect(previous_devices, current_devices)

    database.Save(current_devices)

    print(f"\nCurrent Devices : {len(current_devices)}")
    print(f"Known Devices   : {len(previous_devices)}")
    print(f"New Devices     : {len(new_devices)}\n")

    print("Discovered Devices")
    print("-" * 70)

    for device in current_devices:

        vendor_name = vendor.GetVendor(device.MAC)

        status = "NEW" if device in new_devices else "KNOWN"

        print(
            f"{device.IP:<16}"
            f"{device.MAC:<20}"
            f"{vendor_name:<30}"
            f"{status}"
        )


if __name__ == "__main__":
    RunLANGuard()