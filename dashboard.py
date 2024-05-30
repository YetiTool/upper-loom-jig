import paramiko
import tkinter as tk
from threading import Thread
import time
from datetime import datetime

# SSH details for the three sources
ssh_details = [
    {'hostname': '192.168.200.73', 'port': 22, 'username': 'pi', 'password': 'pi', 'file_path': '/home/pi/upper-loom-jig/RESULTS.txt'},
    {'hostname': '192.168.200.86', 'port': 22, 'username': 'pi', 'password': 'pi', 'file_path': '/home/pi/upper-loom-jig/RESULTS.txt'},
    {'hostname': '192.168.200.65', 'port': 22, 'username': 'pi', 'password': 'pi', 'file_path': '/home/pi/upper-loom-jig/RESULTS.txt'}
]

def read_ssh_file(details):
    """Read a file from an SSH server and return the last 30 lines."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(details['hostname'], port=details['port'], username=details['username'], password=details['password'])
    
    sftp = client.open_sftp()
    file_content = ''
    with sftp.open(details['file_path'], 'r') as file:
        lines = file.readlines()
        # Get the last 30 lines
        last_lines = lines[-30:]
        file_content = ''.join(last_lines)
    
    sftp.close()
    client.close()
    
    return file_content

def update_content():
    """Fetch content from all SSH sources and update the GUI."""
    while True:
        contents = [read_ssh_file(details) for details in ssh_details]
        for i in range(3):
            text_widgets[i].delete('1.0', tk.END)
            text_widgets[i].insert(tk.END, contents[i])
        # Update the timestamp label
        last_updated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamp_label.config(text=f"Last Updated: {last_updated_time}")
        time.sleep(10)

# Create the main window
root = tk.Tk()
root.title("SSH File Viewer")

# Create Text widgets for displaying file contents
text_widgets = [tk.Text(root, wrap=tk.WORD, width=60, height=40, font=('Montserrat', 10)) for _ in range(3)]
for i, text_widget in enumerate(text_widgets):
    text_widget.grid(row=0, column=i, padx=5, pady=5)

# Create a label to display the timestamp of the last update
timestamp_label = tk.Label(root, text="Last Updated: Never", anchor='w', font=('Montserrat', 16))
timestamp_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='w')

# Start the thread to update content
update_thread = Thread(target=update_content, daemon=True)
update_thread.start()

# Start the Tkinter event loop
root.mainloop()