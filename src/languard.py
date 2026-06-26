from scanner import Scanner
from database import Database
from detector import Detector
from vendor import Vendor


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

    for device in current_devices:

        device.Vendor = vendor.GetVendor(device.MAC)

        if device in new_devices:
            device.Status = "New"
        else:
            device.Status = "Known"

    database.Save(current_devices)

    return current_devices