"""
vendor.py

Responsible for vendor lookup.
"""

import csv
from pathlib import Path


class Vendor:

    def __init__(self):

        self.vendors = {}

        csv_path = Path(__file__).parent.parent / "data" / "oui.csv"

        with open(csv_path, newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                self.vendors[row["OUI"]] = row["Vendor"]
    def GetVendor(self, mac: str) -> str:
     oui = mac.upper()[0:8]
     return self.vendors.get(oui, f"Not Cached ({oui})")