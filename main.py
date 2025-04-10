import tkinter as tk
import json
import os
import webbrowser
import pyperclip  # Make sure this is installed: pip install pyperclip

# 47 relative offsets
offsets = [
    [0, 0, 0], [14, 14, 13], [35, 10, -6], [43, 8, -19], [57, 8, -10], [52, 8, 6],
    [51, 8, 28], [36, 8, 54], [16, 14, 48], [18, 13, -17], [31, 25, -19], [33, 15, -31],
    [42, 41, -25], [48, 41, -15], [55, 48, -24], [56, 34, 2], [53, 43, 43], [41, 43, 57],
    [30, 36, 49], [11, 36, 57], [3, 41, 51], [40, -3, 48], [26, -3, 38], [25, 3, 33],
    [17, 3, 31], [27, -3, 22], [20, -3, 16], [37, -9, 1], [53, -9, 8], [58, -10, 25],
    [37, -28, 12], [36, -18, 36], [10, -18, 37], [-13, -27, 27], [-16, -27, 7],
    [-18, -26, -16], [10, -24, -11], [12, -22, -28], [22, -28, -5], [17, -10, -7],
    [-10, -3, 2], [-11, -3, -18], [-24, -3, -25], [1, 0, -28], [-13, 8, 4],
    [-15, 17, -9], [11, 15, 10]
]

# Filename for route file
filename = "skytils_route.txt"

def generate_route(base_x, base_y, base_z):
    route = []
    for i, (dx, dy, dz) in enumerate(offsets[1:], start=1):
        point = {
            "x": base_x + dx,
            "y": base_y + dy,
            "z": base_z + dz,
            "r": 0,
            "g": 1,
            "b": 0,
            "options": {
                "name": str(i)
            }
        }
        route.append(point)
    return route

def save_to_txt(route):
    with open(filename, "w") as f:
        json.dump(route, f, separators=(',', ':'))

def read_file_content():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    return ""

def copy_and_close():
    content = read_file_content()
    pyperclip.copy(content)  # Use pyperclip instead of tkinter clipboard

    copied_label = tk.Label(root, text="Copied!", fg="lime", bg="#1e1e1e", font=("Segoe UI", 10, "bold"))
    copied_label.pack(pady=5)

    root.after(1000, root.destroy)

def open_file():
    if os.path.exists(filename):
        webbrowser.open(f"file://{os.path.abspath(filename)}")

def submit_coords():
    input_text = entry.get()
    try:
        x_str, y_str, z_str = input_text.strip().split()
        x, y, z = int(x_str), int(y_str), int(z_str)
        route = generate_route(x, y, z)
        save_to_txt(route)
        show_copy_window()
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid format. Use: x y z")

def show_copy_window():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#1e1e1e")

    btn_copy_close = tk.Button(root, text="Copy & Close", command=copy_and_close,
                               bg="#333333", fg="#ffffff", activebackground="#444444", relief="flat")
    btn_copy_close.pack(pady=10, ipadx=10, ipady=5)

    btn_open = tk.Button(root, text="Open File", command=open_file,
                         bg="#333333", fg="#ffffff", activebackground="#444444", relief="flat")
    btn_open.pack(pady=5, ipadx=10, ipady=5)

    btn_back = tk.Button(root, text="Back", command=show_entry_window,
                         bg="#333333", fg="#ffffff", activebackground="#444444", relief="flat")
    btn_back.pack(pady=5, ipadx=10, ipady=5)

def show_entry_window():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#1e1e1e")

    label = tk.Label(root, text="Enter base coordinates (x y z):",
                     bg="#1e1e1e", fg="#ffffff")
    label.pack(pady=5)

    global entry
    entry = tk.Entry(root, width=30, bg="#2e2e2e", fg="#ffffff", insertbackground="white")
    entry.pack(pady=5)

    submit_button = tk.Button(root, text="Generate Route", command=submit_coords,
                              bg="#333333", fg="#ffffff", activebackground="#444444", relief="flat")
    submit_button.pack(pady=10, ipadx=10, ipady=5)

# Initialize the main window
root = tk.Tk()
root.title("Skytils Route Generator")
show_entry_window()
root.mainloop()