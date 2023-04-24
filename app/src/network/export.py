__all__ = ['export_to_wireshark','download_pcap_file']
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from .error_handling import handle_error
from scapy.all import wrpcap


# Handles creating and sending of packets. Packet Generation based on packet info.
@handle_error
def export_to_wireshark(result):
    file_path = create_pcap_file(result)
    folder = move_to_selected_folder(file_path)

    # Open the file in Wireshark
    os.startfile(os.path.join(folder, os.path.basename(file_path)))


@handle_error
def create_pcap_file(result):
    file_path = os.path.join(os.getcwd(), "combined_results.pcap")
    
    # Check if file already exists
    if os.path.isfile(file_path):
        # File already exists, prompt user to overwrite or choose a new filename
        overwrite = tk.messagebox.askyesno("File already exists", "A file named 'combined_results.pcap' already exists in the current directory. Do you want to overwrite it?")
        if not overwrite:
            # User chose not to overwrite, prompt user to choose a new filename
            file_path = filedialog.asksaveasfilename(initialfile="combined_results.pcap", defaultextension=".pcap", filetypes=[("PCAP Files", "*.pcap")])
            if not file_path:
                # User canceled file dialog, return None
                return None

    # Write all the packets to the pcap file
    wrpcap(file_path, result)
    
    return file_path

@handle_error
def download_pcap_file(result):
    # Get the default file name
    default_file_name = "combined_results.pcap"

    # Open the file dialog box for saving the file
    file_path = filedialog.asksaveasfilename(initialfile=default_file_name, defaultextension=".pcap", filetypes=[("PCAP Files", "*.pcap")])

    # Check if a file name was entered
    if file_path:
        # Write all the packets to the pcap file
        wrpcap(file_path, result)

        # Move the file to the selected folder
        return file_path
    else:
        # User canceled file dialog, return None
        return None

@handle_error
def move_to_selected_folder(file_path):
    # Create a Tkinter window and hide it
    root = tk.Tk()
    root.withdraw()

    # Get the file name from the file path
    file_name = os.path.basename(file_path)

    # Open a dialog box for the user to enter a new file name
    new_file_name = filedialog.asksaveasfilename(initialfile=file_name)

    # Check if a file name was entered
    if new_file_name:
        # Move the file to the selected directory with the new file name
        shutil.move(file_path, new_file_name)
        return os.path.dirname(new_file_name)
    else:
        return None