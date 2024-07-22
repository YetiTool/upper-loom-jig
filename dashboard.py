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

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

# Create the main window
root = tk.Tk()
root.title("Upper Loom Jig Monitor")

# Make the window fullscreen
root.attributes('-fullscreen', True)
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', exit_fullscreen)

# Create a frame to contain the text widgets
text_frame = tk.Frame(root, bg='#1d1e1f')
text_frame.pack(fill=tk.BOTH, expand=True)

# Create Text widgets for displaying file contents with a specified width
text_widgets = [tk.Text(text_frame, wrap=tk.WORD, font=('Montserrat', 16), bg='#1d1e1f', fg='#ebeef2') for _ in range(3)]
for i, text_widget in enumerate(text_widgets):
    text_widget.grid(row=0, column=i, sticky="nsew")
    text_frame.grid_rowconfigure(0, weight=1)

# Configure weight to make each widget occupy 30% of the screen width
text_frame.grid_columnconfigure(0, weight=1)
text_frame.grid_columnconfigure(1, weight=1)
text_frame.grid_columnconfigure(2, weight=1)


timestamp_frame = tk.Frame(root, bg='#3f4c59')  # Change "#ff0000" to your desired background color
timestamp_frame.pack(side=tk.BOTTOM, fill=tk.X, ipady=10, expand=False)

# Create a label to display the timestamp of the last update with a larger font
timestamp_label = tk.Label(timestamp_frame, text="Last Updated: Never", font=('Montserrat', 16), bg='#3f4c59', fg='#ebeef2')  # Adjust colors as needed
timestamp_label.pack(side=tk.LEFT, padx=5, pady=5)

# Start the thread to update content
update_thread = Thread(target=update_content, daemon=True)
update_thread.start()

# Start the Tkinter event loop
root.mainloop()