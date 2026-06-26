from scanner import Scanner
from database import Database
from detector import Detector
from vendor import Vendor
import socket
def GetHostname(ip):

    try:
        return socket.gethostbyaddr(ip)[0]

    except:
        return "Unknown"
def RunLANGuard():

    scanner = Scanner()

    database = Database()

    detector = Detector()

    vendor = Vendor()

    current_devices = scanner.ScanNetwork()

    previous_devices = database.Load()

    new_devices = detector.Detect(previous_devices, current_devices)

    for device in current_devices:

        device.Hostname = GetHostname(device.IP)
        device.Vendor = vendor.GetVendor(device.MAC)

        if device in new_devices:
            device.Status = "New"
        else:
            device.Status = "Known"

    database.Save(current_devices)

    return current_devices