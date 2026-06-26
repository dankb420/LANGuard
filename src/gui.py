"""
gui.py

Graphical User Interface for LANGuard.
"""
import socket
import subprocess
import tkinter as tk
from tkinter import ttk
from languard import RunLANGuard


class GUI:

    def __init__(self):

        # ---------------- Window ---------------- #

        self.root = tk.Tk()

        self.root.title("LANGuard")

        self.root.geometry("1000x600")

        self.root.minsize(900, 500)

        # ---------------- Frames ---------------- #

        self.topFrame = ttk.Frame(self.root, padding=10)
        self.topFrame.pack(fill="x")

        self.middleFrame = ttk.Frame(self.root, padding=10)
        self.middleFrame.pack(fill="both", expand=True)

        self.bottomFrame = ttk.Frame(self.root, padding=10)
        self.bottomFrame.pack(fill="x")

        # ---------------- Scan Button ---------------- #

        self.scanButton = ttk.Button(
            self.topFrame,
            text="Scan Network",
            command=self.Scan
        )
        # ---------------- Network Information ---------------- #

        self.networkInfo = ttk.Label(
            self.topFrame,
            text=f"Network: {self.GetNetworkName()}    Local IP: {self.GetLocalIP()}"
        )

        self.networkInfo.pack(side="left", padx=20)
        self.scanButton.pack(side="left")

        # ---------------- Status ---------------- #

        self.statusLabel = ttk.Label(
            self.bottomFrame,
            text="Ready."
        )

        self.statusLabel.pack(side="left")

        # ---------------- Tree ---------------- #

        columns = (
            "Hostname",
            "IP",
            "MAC",
            "Vendor",
            "Status",
        )

        self.tree = ttk.Treeview(
            self.middleFrame,
            columns=columns,
            show="headings"
        )
        self.tree.tag_configure(
            "new_device",
            foreground="red"
        )
        self.tree.heading("Hostname", text="Hostname")
        self.tree.heading("IP", text="IP Address")
        self.tree.heading("MAC", text="MAC Address")
        self.tree.heading("Vendor", text="Vendor")
        self.tree.heading("Status", text="Status")
        self.tree.column("Hostname", width=180)
        self.tree.column("IP", width=170)
        self.tree.column("MAC", width=220)
        self.tree.column("Vendor", width=300)
        self.tree.column("Status", width=120)

        scrollbar = ttk.Scrollbar(
            self.middleFrame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    # ------------------------------------------------ #

    def Scan(self):

        self.statusLabel.config(text="Scanning...")
        self.root.update()

        self.tree.delete(*self.tree.get_children())

        devices = RunLANGuard()

        for device in devices:

            status = "🟢 Known"
            tag = ""

            if device.Status == "New":
                status = "🔴 New"
                tag = "new_device"

            self.tree.insert(
                "",
                "end",
                values=(
                    device.Hostname,
                    device.IP,
                    device.MAC,
                    device.Vendor,
                    status
                ),
                tags=(tag,)
            )

        self.statusLabel.config(
            text=f"Scan Complete. {len(devices)} devices found."
        )
            

    # ------------------------------------------------ #

    def Run(self):

        self.root.mainloop()
    def GetLocalIP(self):
        try:
            return socket.gethostbyname(socket.gethostname())
        except:
            return "Unknown"


    def GetNetworkName(self):
        try:
            output = subprocess.check_output(
                "netsh wlan show interfaces",
                shell=True,
                text=True
            )

            for line in output.splitlines():
                if "SSID" in line and "BSSID" not in line:
                    return line.split(":")[1].strip()

        except:
            pass
        return "Wired / Unknown"