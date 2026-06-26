"""
database.py

Responsible for storing and loading discovered devices.
"""
from pathlib import Path
import sqlite3

from device import Device
DATABASE_NAME = Path(__file__).parent.parent / "data" / "languard.db"
class Database:

    def __init__(self):

        self.connection = sqlite3.connect(DATABASE_NAME)

        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Devices(
            MAC TEXT PRIMARY KEY,
            IP TEXT
        )
        """)

        self.connection.commit()


    def Save(self, devices: list[Device]):
        for device in devices:

            self.cursor.execute(
                """
                INSERT OR IGNORE INTO Devices(MAC, IP)
                VALUES(?, ?)
                """,
                (device.MAC, device.IP) 
            )
        self.connection.commit()
    def Load(self) -> list[Device]:

        devices = []

        self.cursor.execute("SELECT IP, MAC FROM Devices")

        rows = self.cursor.fetchall()

        for ip, mac in rows:

            devices.append(Device(ip, mac))

        return devices