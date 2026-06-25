from scanner import Scanner

def Main():

    scanner = Scanner()

    devices = scanner.ScanNetwork()

    print(len(devices))

    for device in devices:
        print(device)


if __name__ == "__main__":
    Main()