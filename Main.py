
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json, os

# ----------------- Data actions -----------------
def save_password():
    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not username or not password:
        messagebox.showwarning("Oops!", "Please don't leave any fields empty!")
        return

    new_data = {website: {"username": username, "password": password}}

    data = {}
    if os.path.exists("data.json"):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            pass

    data.update(new_data)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    messagebox.showinfo("Success", "Password saved!")
    for e in (website_entry, username_entry, password_entry):
        e.delete(0, tk.END)

def find_password():
    website = website_entry.get().strip()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found!")
        return

    if website in data:
        u, p = data[website]["username"], data[website]["password"]
        messagebox.showinfo(website, f"Username: {u}\nPassword: {p}")
    else:
        messagebox.showwarning("Not Found", f"No details for '{website}'.")

# ----------------- UI -----------------
root = tk.Tk()
root.title("Password Manager")
root.geometry("700x500")
root.config(padx=16, pady=16)

# Let columns expand
for c in range(3):
    root.grid_columnconfigure(c, weight=1)

# ---- Header with image that covers full width ----
HEADER_H = 150  # header height in pixels
header = tk.Frame(root, height=HEADER_H)
header.grid(row=0, column=0, columnspan=3, sticky="nsew")
header.grid_propagate(False)  # keep fixed height

header_label = tk.Label(header)
header_label.pack(fill="both", expand=True)

# Load original image once
# Replace 'logo.png' with your file (PNG/JPG)
orig = Image.open("img.png")

def cover_resize(img, target_w, target_h):
    """Resize + crop center to fill target (like CSS background-size: cover)."""
    iw, ih = img.size
    scale = max(target_w / iw, target_h / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    resized = img.resize((max(1, nw), max(1, nh)), Image.LANCZOS)
    left = (nw - target_w) // 2
    top = (nh - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))

def refresh_header(_=None):
    # Use header's current width to fill; keep fixed height
    w = header.winfo_width() or root.winfo_width()
    if w <= 1:
        return
    banner = cover_resize(orig, w, HEADER_H)
    photo = ImageTk.PhotoImage(banner)
    header_label.config(image=photo)
    header_label.image = photo  # keep reference

root.bind("<Configure>", refresh_header)
root.after(50, refresh_header)  # first paint

# ---- Form ----
tk.Label(root, text="Website:", font=("Arial", 12)).grid(row=1, column=0, pady=6, sticky="e")
tk.Label(root, text="Username/Email:", font=("Arial", 12)).grid(row=2, column=0, pady=6, sticky="e")
tk.Label(root, text="Password:", font=("Arial", 12)).grid(row=3, column=0, pady=6, sticky="e")

website_entry = tk.Entry(root)
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

website_entry.grid(row=1, column=1, sticky="ew", padx=6)
username_entry.grid(row=2, column=1, sticky="ew", padx=6)
password_entry.grid(row=3, column=1, sticky="ew", padx=6)
website_entry.focus()

tk.Button(root, text="Search", command=find_password).grid(row=1, column=2, padx=6)
tk.Button(root, text="Save", command=save_password).grid(row=4, column=2, padx=6, pady=12, sticky="e")

root.mainloop()


