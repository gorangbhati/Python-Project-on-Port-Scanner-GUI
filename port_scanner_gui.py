import tkinter as tk
from tkinter import scrolledtext, messagebox
import socket
import threading

window = tk.Tk()
window.title("Port Scanner")

tk.Label(window, text="Target IP:").grid(row=0, column=0, padx=5, pady=5)
target_entry = tk.Entry(window, width=30)
target_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Start Port:").grid(row=1, column=0, padx=5, pady=5)
start_entry = tk.Entry(window, width=10)
start_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(window, text="End Port:").grid(row=2, column=0, padx=5, pady=5)
end_entry = tk.Entry(window, width=10)
end_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(window, text="Scan Type:").grid(row=3, column=0, padx=5, pady=5)
scan_type_var = tk.StringVar(window)
scan_type_var.set("tcp")
scan_type_menu = tk.OptionMenu(window, scan_type_var, "tcp", "udp")
scan_type_menu.grid(row=3, column=1, padx=5, pady=5)

output_text = scrolledtext.ScrolledText(window, width=60, height=20)
output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

def scan_port(target_ip, port, scan_type="tcp"):
    try:
        if scan_type == "tcp":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                output_text.insert(tk.END, f"Port {port}: Open (TCP)\n")
            else:
                output_text.insert(tk.END, f"Port {port}: Closed (TCP)\n")
            sock.close()
        elif scan_type == "udp":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            sock.sendto(b"", (target_ip, port))
            try:
                data, addr = sock.recvfrom(1024)
                output_text.insert(tk.END, f"Port {port}: Open (UDP)\n")
            except socket.timeout:
                output_text.insert(tk.END, f"Port {port}: Open/Filtered (UDP)\n")
            except Exception as e:
                output_text.insert(tk.END, f"Port {port}: Closed (UDP) or Error : {e}\n")
            sock.close()

    except socket.gaierror:
        messagebox.showerror("Error", "Hostname could not be resolved.")
    except socket.error as e:
        output_text.insert(tk.END, f"Could not connect to {target_ip}:{port}. Error: {e}\n")

def start_scan():
    target_ip = target_entry.get()
    try:
        start_port = int(start_entry.get())
        end_port = int(end_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid port range.")
        return

    scan_type = scan_type_var.get()
    output_text.delete(1.0, tk.END)

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port, scan_type))
        thread.start()

scan_button = tk.Button(window, text="Scan", command=start_scan)
scan_button.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()