How to Run This Project (Step-by-Step)

1️⃣ Install Python

Download from:
https://www.python.org/downloads/

Make sure to enable Add to PATH.

2️⃣ Clone or Download the Repository
git clone https://github.com/your-username/port-scanner-gui.git

cd port-scanner-gui


Or extract the ZIP file manually.

3️⃣ Run the Script
python port_scanner_gui.py


The GUI window will open.

🖥 How to Use the Application
➤ 1. Enter Target IP

Example:

127.0.0.1

192.168.1.10

or any valid server/domain

➤ 2. Enter Port Range

Example:

Start Port → 1

End Port → 100

➤ 3. Select Scan Type

TCP

UDP

➤ 4. Click “Scan”

Results appear in the scrollable output box.

🧠 How It Works (Based on Source Code)

The Script Uses:

✔ socket for network operations
✔ threading.Thread to scan each port concurrently
✔ Tkinter widgets:

Entry

OptionMenu

ScrolledText

Button

Port Discovery Logic:

TCP → connect_ex() checks if port accepts connection

UDP → send packet & wait for response (Timeout = Filtered)

⚠ Disclaimer

This tool is for educational and ethical testing only.
Scanning systems without permission is illegal.

📄 License

Free for educational, learning, and ethical use.
